import logging

from django.conf import settings
from django.http import Http404
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Display the home page of the application.
    """
    logger.info("Requesting index")
    return render(request, "index.html")


def custom_404(request, exception):
    logger.info("Requesting custom error page 404")
    return render(request, "404.html", status=404)


def custom_500(request):
    logger.info("Requesting custom error page 500")
    return render(request, "500.html", status=500)


# Views used only for testing error handlers
def test_500(request):
    raise Exception("Test erreur 500 volontaire")


def test_404(request):
    raise Http404("Test erreur 404 volontaire")


# View use only for testing sentry
def sentry_debug(request):
    if not settings.DEBUG:
        raise Http404
    1 / 0
