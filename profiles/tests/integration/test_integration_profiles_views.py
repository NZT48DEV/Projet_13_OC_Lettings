from django.urls import reverse

from profiles.models import Profile
from tests.helpers import assert_custom_error_page


def test_profiles_index_page(db, client):
    response = client.get("/profiles/")
    assert_custom_error_page(response, 200, "profiles/index.html", "Profiles")


def test_profile_detail_page(db, client, profile: Profile):
    url = reverse("profiles:profile", kwargs={"username": profile.user.username})
    response = client.get(url)
    assert_custom_error_page(
        response, 200, "profiles/profile.html", profile.favorite_city
    )


def test_profile_detail_404(db, client):
    url = reverse("profiles:profile", kwargs={"username": "Unknown-user"})
    response = client.get(url)
    assert response.status_code == 404
