from django.test import override_settings


def test_non_existing_url_returns_custom_404_page(client):
    response = client.get("/url-qui-nexistera-jamais/")
    assert response.status_code == 404

    if response.templates:
        names = [t.name for t in response.templates]
        assert "404.html" in names

    assert "<h1" in response.text
    assert "</h1>" in response.text

    h1 = response.text.split("<h1", 1)[1].strip()
    after_h1 = h1.split(">", 1)[1]
    h1_content = after_h1.split("</h1>", 1)[0]
    assert "Erreur 404" in h1_content


@override_settings(DEBUG=False, DEBUG_PROPAGATE_EXCEPTIONS=False)
def test_custom_500_page(client):
    client.raise_request_exception = False
    response = client.get("/test-500/")
    assert response.status_code == 500

    if response.templates:
        names = [t.name for t in response.templates]
        assert "500.html" in names

    assert "<h1" in response.text
    assert "</h1>" in response.text

    h1 = response.text.split("<h1", 1)[1].strip()
    after_h1 = h1.split(">", 1)[1]
    h1_content = after_h1.split("</h1>", 1)[0]
    assert "Erreur 500" in h1_content
