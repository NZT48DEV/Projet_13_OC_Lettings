from django.http import Http404
from django.shortcuts import render


def index(request):
    """
    Display the home page of the application.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


# Views used only for testing error handlers
def test_500(request):
    raise Exception("Test erreur 500 volontaire")


def test_404(request):
    raise Http404("Test erreur 404 volontaire")
