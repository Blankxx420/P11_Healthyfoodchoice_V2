import time

import requests


class Openfoodfact:

    def __init__(self):
        self.payload = {
            "search_simple": 1,
            "action": "process",
            "tagtype_0": "countries",
            "tag_contains_0": "contains",
            "tag_0": "france",
            "sort_by": "unique_scans_n",
            "page_size": 750,
            "json": 1,
            # field make the request faster
            "fields": "product_name_fr,code,brands,nutriscore_grade,url,"
            "image_url,image_small_url,nutriments,categories",
        }
        self.products = []
        self.get_product()

    def get_product(self):
        r = ""
        while r == "":
            try:
                r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?",
                                 params=self.payload,
                                 )
                break
            except ValueError:
                time.sleep(5)
                continue
        if r.status_code == 200:
            self.products = r.json()["products"]
        else:
            error = f" error code is: {r.status_code}"
            print(error)

    def avoid_empty(self):
        full_product = []
        for product in self.products:
            if None not in (
                product.get("product_name_fr"),
                product.get("code"),
                product.get("brands"),
                product.get("nutriscore_grade"),
                product.get("url"),
                product.get("image_url"),
                product.get("image_small_url"),
                product.get("categories"),
                product.get("nutriments")
            ):

                full_product.append(product)
        return full_product


op = Openfoodfact()
op.avoid_empty()
