"""Views for the catalog application."""

from django.shortcuts import render


def catalog_view(request):
    """
    Render the catalog page showing available products.

    [Punto 13] View returning the catalog template.
    """
    return render(request, 'catalog/catalog.html')
