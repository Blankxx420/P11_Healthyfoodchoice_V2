from django.test import TestCase
from search.models.category import Categories
from search.models.product import Product
from search.models.substitute import Substitute
from users.models import User


class CategoryTest(TestCase):

    def test_category_str(self):
        self.cat = Categories.objects.create(name="Snack")
        self.assertEqual(str(self.cat), "Snack")


class ProductTest(TestCase):

    def test_product_str(self):
        product = Product.objects.create(
            name="Prince",
            barcode=7622210449283,
            url="https://fr.openfoodfacts.org/produit/7622210449283/prince-lu",
            url_image="https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.400.jpg",
            url_image_small="https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.200.jpg",
            brands="Lu, Prince, Mondelez",
            nutrition_score="d",
            energy_100g=0.0,
            sugars_100g=4.8,
            sodium_100g=4.04,
            fat_100g=1.6,
            salt_100g=0.1,
        )
        self.assertEqual(str(product), "Prince, d")


class SubstituteTest(TestCase):

    def setUp(self):
        self.prd = Product.objects.create(name="Prince", barcode="7622210449283", nutrition_score="D")
        self.substitute = Product.objects.create(name="Biscuit sésame", barcode="3175680011480", nutrition_score="C")
        self.user = User.objects.create(username='jacob', email='jacob@hotmail.fr', password="oiseau21")
        self.favorite = Substitute.objects.create(product_id=self.prd, substitute_id=self.substitute,
                                                  user_id=self.user)

    def test_favorite_str(self):
        self.assertEqual(str(self.favorite), f"Produit: {self.prd}, Substitut: {self.substitute}"
                                             f", User: {self.user}")
