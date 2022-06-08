from django.test import Client, TestCase
from search.models.product import Product


class TestCompleteView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_using_product_autocompletion(self):
        Product.objects.create(name="Nutella", id=3)
        response = self.client.get("/autocomplete/?term=nutel")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'[{"name": "Nutella", "id": 3}]')


