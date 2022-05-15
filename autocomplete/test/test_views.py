from django.test import Client, TestCase


class TestCompleteView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_using_product_autocompletion(self):
        response = self.client.get("/autocomplete/?term=nutel")
        self.assertEqual(response.status_code, 200)


