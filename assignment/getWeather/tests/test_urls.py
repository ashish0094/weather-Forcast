from django.test import SimpleTestCase
from django.urls import reverse, resolve
from getWeather.views import home, forcastData

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, home)

    def test_list_url_is_resolved(self):
        url = reverse('data')
        self.assertEquals(resolve(url).func, forcastData)


