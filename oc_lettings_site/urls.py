from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("test-404/", views.test_404, name="test_404"),
    path("test-500/", views.test_500, name="test_500"),
    path("sentry-debug/", views.sentry_debug),
]

handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"
