from django.db import models

class weatherData(models.Model):
    Latitude = models.FloatField(max_length=10)
    Longitude = models.FloatField(max_length=10)
    temperature = models.FloatField(max_length=5)

