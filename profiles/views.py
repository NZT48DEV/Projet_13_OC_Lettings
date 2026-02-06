import logging

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of all user profiles.
    """
    logger.info("Requesting index")

    profiles_list = Profile.objects.all()

    logger.info("Requesting profiles_list : %s items", profiles_list.count())

    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display the details of a single user profile.
    """
    logger.info(
        "Requesting profile detail (username=%s)",
        username,
    )
    try:
        profile_obj = get_object_or_404(Profile, user__username=username)
    except Http404:
        logger.warning("username=%s not found", username, extra={"username": username})
        raise

    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
