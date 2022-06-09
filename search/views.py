from django.db.models import Count
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from search.search_form import Searchbar
from search.models.product import Product
from search.models.category import Categories
from search.models.substitute import Substitute
from users.models import User


def home(request):
    search_bar = Searchbar()
    context = {
        "searchbar": search_bar
    }
    return render(request, 'search/home.html', context)


def products(request):
    if request.method == "POST":
        product_search = request.POST["product_search"]
        products_obj = Product.objects.all().filter(
            name__contains=product_search.strip().lower().capitalize()
        )[:6]
        print(products_obj)
        context = {
            # title in HTML will contain value of product_search
            "title": product_search,
            "products": products_obj,
        }
        print(context)
        # send context to products.html template and render this template
        return render(request, "search/products.html", context)


def product(request, product_id):
    """Displays the product details page
    Args:
        request: base parameter
        product_id (int): Id of the product
    """
    # try:
    product_obj = Product.objects.get(pk=product_id)
    context = {"product": product_obj}
    # except Product.DoesNotExist:
    print(context)
    return render(request, "search/product.html", context)


def substitutes(request, product_id):
    """ Display substitutes from selected product"""
    # Find product searched by user with id
    product_query = Product.objects.get(pk=product_id)

    # Find the category of the product
    product_query_cat = Categories.objects.filter(product__id=product_query.id)

    # Find 9 products with better nutrition_score in the same category
    substitutes_prod = (
        Product.objects.filter(category__in=product_query_cat)
        .annotate(nb_cat=Count("category"))
        .filter(nb_cat__gte=3)
        .filter(nutrition_score__lt=product_query.nutrition_score)
        .order_by("nutrition_score")[:9]
    )

    context = {"product": product_query, "substitutes": substitutes_prod}

    return render(request, "search/substitutes.html", context)


@login_required
def save_favorite(request, product_id, substitute_id):
    """ save the product and the substitute chosen for the user """
    product_query = Product.objects.get(pk=product_id)
    substitute_query = Product.objects.get(pk=substitute_id)
    user = User.objects.get(pk=request.user.id)
    favorite = Substitute(product_id_id=product_query.id, substitute_id_id=substitute_query.id, user_id_id=user.id)
    try:
        favorite.save()
        return redirect("search:favorites")
    except IntegrityError:
        return redirect("search:home")


@login_required
def favorites(request):
    """Display Favorites page of the user"""
    favorites_prod = Substitute.objects.filter(user_id_id=request.user.id)
    context = {
        "favorites": favorites_prod
    }
    return render(request, "search/favorites.html", context)


def legal_notice(request):
    return render(request, "search/legal_notice.html")
