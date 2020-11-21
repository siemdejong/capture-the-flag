from django.urls import path
from ctf_game import views

urlpatterns = [
    path("", views.home, name="home"),
]