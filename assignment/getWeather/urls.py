from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name= 'list'),
    path('data', views.forcastData, name='data')
]