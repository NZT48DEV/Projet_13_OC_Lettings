from django.test import override_settings


def test_non_existing_url_returns_custom_404_page(client):
    response = client.get("/url-qui-nexistera-jamais/")
    assert response.status_code == 404

    names = [t.name for t in response.templates]
    assert "404.html" in names

    assert "Erreur 404" in response.text


@override_settings(DEBUG=False, DEBUG_PROPAGATE_EXCEPTIONS=False)
def test_custom_500_page(client):
    client.raise_request_exception = False
    response = client.get("/test-500/")
    assert response.status_code == 500

    names = [t.name for t in response.templates]
    assert "500.html" in names

    assert "Erreur 500" in response.text
