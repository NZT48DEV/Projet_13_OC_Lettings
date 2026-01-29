from django.shortcuts import render, get_object_or_404
from .models import Profile

def index(request):
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)

def profile(request, username):
    profile_obj = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
