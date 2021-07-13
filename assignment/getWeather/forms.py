from django import forms

class coordinates(forms.Form):
    Latitude = forms.FloatField(max_value=90.0, min_value=-90.0)
    Longitude = forms.FloatField(max_value=180.0, min_value=-180.0)
