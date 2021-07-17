from django.http import response
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from getWeather.models import weatherData
import json

class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        return super().setUp()

    def test_home(self):
        response = self.client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_forcastData_valid(self):

        response = self.client.post(reverse('data'), {
            'Latitude': 41.8781,
            'Longitude': -87.6298
        })

        self.assertEquals(response.status_code, 200)

    def test_forcastData_lat_invalid(self):

        response = self.client.post(reverse('data'), {
            'Latitude': 140.6331,
            'Longitude': -89.3985
        })

        self.assertEquals(response.status_code, 500)
    

    def test_forcastData_longi_invalid(self):

        response = self.client.post(reverse('data'), {
            'Latitude': 40.6331,
            'Longitude': -189.3985
        })

        self.assertEquals(response.status_code, 500)

    def test_forcastData_both_invalid(self):

        response = self.client.post(reverse('data'), {
            'Latitude': 140.6331,
            'Longitude': -189.3985
        })

        self.assertEquals(response.status_code, 500)

    
    def test_forcastData_Not_of_usa(self):

        response = self.client.post(reverse('data'), {
            'Latitude': 28.7041,
            'Longitude': 77.1025
        })

        self.assertTemplateUsed(response, 'second.html')