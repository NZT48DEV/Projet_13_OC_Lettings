import pytest
from django.contrib.auth import get_user_model
from django.test import RequestFactory

from oc_lettings_site.views import sentry_debug
from tests.helpers import assert_custom_error_page


@pytest.fixture
def staff_user(db):
    User = get_user_model()
    user = User.objects.create_user(username="staff", password="pass")
    user.is_staff = True
    user.save()
    return user


def test_custom_404_page(client, monkeypatch, staff_user):
    # Activer les routes de démo + login staff (sinon redirection /admin/login/)
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "true")
    client.force_login(staff_user)

    response = client.get("/test-404/")
    assert_custom_error_page(response, 404, "404.html", "Erreur 404")


def test_custom_500_page(client, monkeypatch, staff_user):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "true")
    client.force_login(staff_user)

    client.raise_request_exception = False
    response = client.get("/test-500/")
    assert_custom_error_page(response, 500, "500.html", "Erreur 500")


def test_oc_lettings_site_index(client):
    response = client.get("/")
    assert_custom_error_page(response, 200, "index.html", "Welcome to Holiday Homes")


def test_non_existing_url_returns_custom_404_page(client):
    response = client.get("/url-qui-nexistera-jamais/")
    assert_custom_error_page(response, 404, "404.html", "Erreur 404")


def test_sentry_debug_raises_zero_division_when_demo_enabled(monkeypatch, staff_user):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "true")

    request = RequestFactory().get("/sentry-debug/")
    request.user = staff_user

    with pytest.raises(ZeroDivisionError):
        sentry_debug(request)


def test_sentry_debug_returns_500_when_demo_enabled(client, monkeypatch, staff_user):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "true")
    client.force_login(staff_user)

    client.raise_request_exception = False
    response = client.get("/sentry-debug/")
    assert response.status_code == 500


def test_sentry_debug_returns_404_when_demo_disabled(client, monkeypatch, staff_user):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "false")
    client.force_login(staff_user)

    response = client.get("/sentry-debug/")
    assert response.status_code == 404


def test_demo_routes_redirect_to_admin_login_when_not_logged_in(client, monkeypatch):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "true")

    response = client.get("/sentry-debug/")
    assert response.status_code == 302
    assert "/admin/login/" in response["Location"]


def test_test_404_returns_404_when_demo_disabled(client, monkeypatch, staff_user):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "false")
    client.force_login(staff_user)

    response = client.get("/test-404/")
    assert response.status_code == 404


def test_test_500_returns_404_when_demo_disabled(client, monkeypatch, staff_user):
    monkeypatch.setenv("ENABLE_DEMO_ROUTES", "false")
    client.force_login(staff_user)

    response = client.get("/test-500/")
    assert response.status_code == 404
