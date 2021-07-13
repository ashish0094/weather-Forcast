from django.contrib import admin
from .models import weatherData

@admin.register(weatherData)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Latitude', 'Longitude', 'temperature')


