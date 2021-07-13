from . import views
from django.urls import path

urlpatterns = [
    path("", views.home),
    path('data', views.forcastData)
]