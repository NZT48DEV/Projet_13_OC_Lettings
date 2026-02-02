from django.shortcuts import get_object_or_404, render

from .models import Profile


def index(request):
    """
    Display the list of all user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display the details of a single user profile.
    """
    profile_obj = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
