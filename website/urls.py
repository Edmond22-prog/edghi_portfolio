from django.urls import path

from website.views.base import base

urlpatterns = [
    path("", base, name="base"),
]
