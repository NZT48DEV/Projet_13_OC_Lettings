import pytest
from django.test import RequestFactory, override_settings

from oc_lettings_site.views import sentry_debug
from tests.helpers import assert_custom_error_page


def test_custom_404_page(client):
    response = client.get("/test-404/")
    assert_custom_error_page(response, 404, "404.html", "Erreur 404")


def test_custom_500_page(client):
    client.raise_request_exception = False
    response = client.get("/test-500/")
    assert_custom_error_page(response, 500, "500.html", "Erreur 500")


def test_oc_lettings_site_index(client):
    response = client.get("/")
    assert_custom_error_page(response, 200, "index.html", "Welcome to Holiday Homes")


def test_non_existing_url_returns_custom_404_page(client):
    response = client.get("/url-qui-nexistera-jamais/")
    assert_custom_error_page(response, 404, "404.html", "Erreur 404")


@override_settings(DEBUG=True)
def test_sentry_debug_raises_zero_division():
    request = RequestFactory().get("/sentry-debug/")
    with pytest.raises(ZeroDivisionError):
        sentry_debug(request)


@override_settings(DEBUG=True)
def test_sentry_debug_returns_500(client):
    client.raise_request_exception = False
    response = client.get("/sentry-debug/")
    assert response.status_code == 500


@override_settings(DEBUG=False)
def test_sentry_debug_returns_404(client):
    response = client.get("/sentry-debug/")
    assert response.status_code == 404
