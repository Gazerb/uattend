# External Imports
from django.shortcuts import render


def index(request):
    """A view to load index page"""

    return render(request, "home/index.html")