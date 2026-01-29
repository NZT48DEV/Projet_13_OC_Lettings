from django.shortcuts import render, get_object_or_404
from .models import Letting

def index(request):
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)

def letting(request, letting_id):
    letting_obj = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting_obj.title,
        "address": letting_obj.address,
    }
    return render(request, "lettings/letting.html", context)
