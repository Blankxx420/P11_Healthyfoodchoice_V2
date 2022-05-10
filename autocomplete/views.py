from django.http import JsonResponse

from search.models import Product


def complete(request):
    """Displays product(s) that contains user's entry
    Args:
        term (str): User's entry in search forms"""
    searched_term = request.GET.get("term")
    query_set = Product.objects.get_all_by_term(searched_term)
    products = [
        {
            # how display name according to length
            "name": product.name[:30] + "..."
            if len(product.name) > 33
            else product.name,
            "id": product.id,
        }
        for product in query_set
    ]
    # False as it is not a dict but a list
    return JsonResponse(products, safe=False)