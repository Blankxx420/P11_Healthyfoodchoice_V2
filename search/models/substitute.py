from django.db import models
from .product import Product
from users.models import User


class Substitute(models.Model):

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorite_product")
    substitute_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorite_substitute")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_user")

    def __str__(self):
        return (
            f"Produit: {self.product_id}, Substitut: {self.substitute_id}, User: {self.user_id}"
        )
