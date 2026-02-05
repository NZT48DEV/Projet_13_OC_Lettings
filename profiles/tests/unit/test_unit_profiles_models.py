from profiles.models import Profile


def test_str_profiles(profile: Profile):
    result = str(profile)
    assert result == profile.user.username
