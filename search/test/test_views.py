from django.test import TestCase, Client
from django.urls import reverse
from search.models.product import Product
from users.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username="user1",
            email="user1@gmail.com",
            password="password1234",
        )
        Product.objects.create(id=713, name="Nutella biscuits", nutrition_score="E")
        self.url_home = reverse('search:home')
        self.url_product = reverse('search:product', args=[713])
        self.url_products = reverse('search:products')
        self.url_substitutes = reverse('search:substitutes', args=[713])
        self.url_favorites = reverse('search:favorites')
        self.url_legal_notice = reverse('search:legal_notice')

    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/home.html')
        self.assertContains(response, "product_search")

    def test_products_page_POST(self):
        product_search = {"product_search": "input"}

        response = self.client.post(
            self.url_products, data=product_search
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/products.html")

    def test_product_details_page(self):
        response = self.client.get(self.url_product)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].name, "Nutella biscuits")
        self.assertTemplateUsed(response, "search/product.html")

    def test_substitutes_page(self):
        response = self.client.get(self.url_substitutes)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/substitutes.html")

    def test_save_substitute_as_favorite_success(self):
        self.client.force_login(self.user)
        product = Product.objects.create(
            name="Oasis framboise", nutrition_score="E", barcode="1231231231231"
        )
        substitute = Product.objects.create(
            name="Maytea fraise", nutrition_score="C", barcode="7897897897897"
        )
        # print(f"product.id: {product.id} / substitute.id: {substitute.id}")
        url = reverse(
            "search:save_favorite",
            args=(
                product.id,
                substitute.id,
            ),
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_favorites_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url_favorites)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/favorites.html")

    def test_legal_notice_page(self):
        response = self.client.get(self.url_legal_notice)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/legal_notice.html")
