from django.urls import reverse

from lettings.models import Letting
from tests.helpers import assert_custom_error_page


def test_lettings_index_page(db, client):
    response = client.get("/lettings/")
    assert_custom_error_page(response, 200, "lettings/index.html", "Lettings")


def test_letting_detail_page(db, client, letting: Letting):
    url = reverse("lettings:letting", kwargs={"letting_id": letting.id})
    response = client.get(url)
    assert_custom_error_page(response, 200, "lettings/letting.html", letting.title)


def test_letting_detail_404(db, client, letting: Letting):
    url = reverse("lettings:letting", kwargs={"letting_id": letting.id + 1})
    response = client.get(url)
    assert response.status_code == 404
