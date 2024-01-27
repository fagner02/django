from django.contrib import admin
from django.urls import path, include
from django_app.views import index

urlpatterns = [
    path("", index),
]
from django.urls import path
