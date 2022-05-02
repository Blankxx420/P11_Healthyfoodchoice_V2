"""this file represent admin site models"""
from django.contrib import admin
from search.models.product import Product
from search.models.substitute import Substitute
from search.models.category import Categories


admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Substitute)

