import pytest
from django.core.exceptions import ValidationError

from profiles.models import Profile


def test_favorite_city_accept_empty_string(user):
    favorite_city_obj = Profile.objects.create(user=user, favorite_city="")
    favorite_city_obj.full_clean()


def test_favorite_city_refuse_string_too_long(user):
    favorite_city_obj = Profile.objects.create(user=user, favorite_city="X" * 65)
    with pytest.raises(ValidationError):
        favorite_city_obj.full_clean()
