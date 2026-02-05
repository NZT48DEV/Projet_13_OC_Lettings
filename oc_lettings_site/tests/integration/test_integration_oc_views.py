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
