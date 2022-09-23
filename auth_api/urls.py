from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('auth_token', views.auth_token, name="get_token")
]