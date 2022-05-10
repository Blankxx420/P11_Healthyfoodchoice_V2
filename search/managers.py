from django.db import models


class ProductManager(models.Manager):
    def get_all_by_term(self, term):
        return self.filter(name__icontains=term)
