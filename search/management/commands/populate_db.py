from django.db import IntegrityError
from django.core.management import BaseCommand
from search.openfoodfact import Openfoodfact
from search.models.substitute import Substitute
from search.models.category import Categories
from search.models.product import Product
from progress.bar import Bar


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clear_db()
        op = Openfoodfact()
        products = op.avoid_empty()
        if products is not None:
            self.stdout.write(
                self.style.SUCCESS("La récupération des donnés est bien réussi !")
            )
        if products is None:
            self.stdout.write(
                self.style.ERROR("Echec de la récuperation des données")
            )
            return
        with Bar(
            "Inserting data in databases...", max=len(products), suffix='%(percent)d%%'
        ) as bar:
            for product in products:
                name = product.get("product_name_fr")[:150].strip().lower().capitalize()
                brands = product.get("brands")[:150].upper()
                barcode = product.get("code")[:13].strip()
                url = product.get("url")
                image_url = product.get("image_url")
                image_small_url = product.get("image_small_url")
                nutriscore = product.get("nutriscore_grade")[0].upper()
                categories = [
                    name.strip().lower().capitalize()
                    for name in product["categories"].split(",")
                ]

                # Get some of the nutriments keys/values
                nutriments_list = [
                    "energy_100g",
                    "sugars_100g",
                    "sodium_100g",
                    "fat_100g",
                    "salt_100g",
                ]

                nutriments_dict = {}
                for nutriment in nutriments_list:
                    nutriment_value = product.get("nutriments").get(nutriment)
                    if isinstance(nutriment_value, float) is True:
                        value = nutriment_value
                    else:
                        value = 0
                    nutriments_dict[nutriment] = value

                product_obj = Product(
                    name=name,
                    brands=brands,
                    barcode=barcode,
                    url=url,
                    url_image=image_url,
                    url_image_small=image_small_url,
                    nutrition_score=nutriscore,
                    energy_100g=nutriments_dict.get("energy_100g"),
                    sugars_100g=nutriments_dict.get("sugars_100g"),
                    sodium_100g=nutriments_dict.get("sodium_100g"),
                    fat_100g=nutriments_dict.get("fat_100g"),
                    salt_100g=nutriments_dict.get("salt_100g"),
                )

                try:
                    product_obj.save()

                    # Save categories, linking them to Product obj
                    saved_categories = []
                    for category in categories:
                        cat_obj = Categories(name=category)
                        if category not in saved_categories:
                            # Avoid duplicated categories
                            saved_categories.append(category)
                            try:
                                cat_obj.save()
                            except IntegrityError:  # Avoid duplicated cat
                                cat_obj = Categories.objects.get(name=category)
                            # add() Django method to link manytomany relation
                            product_obj.category.add(cat_obj)
                            product_obj.save()

                except IntegrityError:
                    continue
                bar.next()

    def clear_db(self):
        """functions to clear database before insertions """
        product_objects = Product.objects.all()
        product_objects.delete()

        category_objects = Categories.objects.all()
        category_objects.delete()

        substitutes_objects = Substitute.objects.all()
        substitutes_objects.delete()
