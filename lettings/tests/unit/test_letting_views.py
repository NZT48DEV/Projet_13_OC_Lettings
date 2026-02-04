from django.urls import reverse

from lettings.models import Letting


def test_lettings_index_page(db, client):
    response = client.get("/lettings/")
    assert response.status_code == 200

    names = [t.name for t in response.templates]
    assert "lettings/index.html" in names

    assert "Lettings" in response.text


def test_letting_detail_page(db, client, letting: Letting):
    url = reverse("lettings:letting", kwargs={"letting_id": letting.id})
    response = client.get(url)
    assert response.status_code == 200

    names = [t.name for t in response.templates]
    assert "lettings/letting.html" in names

    assert letting.title in response.text


def test_letting_detail_404(db, client, letting: Letting):
    url = reverse("lettings:letting", kwargs={"letting_id": letting.id + 1})
    response = client.get(url)
    assert response.status_code == 404
