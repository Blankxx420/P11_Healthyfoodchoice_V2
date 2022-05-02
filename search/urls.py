from django.urls import path
from . import views

app_name = "search"
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("substitutes/<int:product_id>/",
         views.substitutes, name="substitutes"),
    path("save_favorite/<int:product_id>/<int:substitute_id>/",
         views.save_favorite, name="save_favorite"),
    path("favorites/",
         views.favorites, name="favorites"),
    path("legal_notice/", views.legal_notice, name="legal_notice")
]
