from search.search_form import NavSearchForm


def navigation_search_form(request):
    """Instanciate search form on the navigation bar"
    Args:
        request (obj): An Http request object
    Returns:
        dict: Dict of elements that gets added to the context of a template
    """
    nav_search_form = NavSearchForm()  # instanciate form
    context = {
        # key: variables we access from template
        "nav_search_form": nav_search_form,
    }

    return context