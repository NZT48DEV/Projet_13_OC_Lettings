from django.shortcuts import render


def index(request):
    """
    Display the home page of the application.
    """
    return render(request, "index.html")
