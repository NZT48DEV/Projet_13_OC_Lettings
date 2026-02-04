import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def user(db):
    user_obj = User.objects.create_user("Fred", "fred@test.com", "fredpassword")
    return user_obj


@pytest.fixture
def profile(db, user):
    profile_obj = Profile.objects.create(user=user)
    return profile_obj
