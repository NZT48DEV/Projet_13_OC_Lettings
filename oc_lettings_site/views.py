import logging
import os

from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render

logger = logging.getLogger(__name__)


def demo_routes_enabled() -> bool:
    return os.getenv("ENABLE_DEMO_ROUTES", "false").lower() == "true"


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


@staff_member_required
def test_500(request):
    if not demo_routes_enabled():
        raise Http404()
    raise Exception("Test erreur 500 volontaire")


@staff_member_required
def test_404(request):
    if not demo_routes_enabled():
        raise Http404()
    raise Http404("Test erreur 404 volontaire")


# View use only for testing sentry
@staff_member_required
def sentry_debug(request):
    if not demo_routes_enabled():
        raise Http404()
    1 / 0
