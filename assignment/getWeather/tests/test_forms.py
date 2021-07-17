from django.test import SimpleTestCase
from getWeather.forms import coordinates

class TestForms(SimpleTestCase):

    def test_coordinates_form_valid_data(self):
        form = coordinates(data={
            'Latitude': 40.6331,
            'Longitude': -89.3985
        })

        self.assertTrue(form.is_valid())
    
    def test_coordinates_form_no_data(self):
        form = coordinates(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals((len(form.errors)), 2)

    def test_coordinates_form_check_max_value(self):
        form = coordinates(data={
            'Latitude': 92.3425,
            'Longitude': 179.4325
        })

        self.assertFalse(form.is_valid())
        self.assertEquals((len(form.errors)), 1)

    def test_coordinates_form_check_min_value(self):
        form = coordinates(data={
            'Latitude': -92.3425,
            'Longitude': 179.4325
        })

        self.assertFalse(form.is_valid())
        self.assertEquals((len(form.errors)), 1)
    