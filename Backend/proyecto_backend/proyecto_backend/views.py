"""Project-level views handling core landing pages."""

from django.shortcuts import render


def homepage(request):
    """
    Render the homepage of the project.
    [Punto 1 y 5] Returns the home.html template.
    """
    return render(request, 'home.html')