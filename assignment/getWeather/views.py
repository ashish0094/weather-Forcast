from django.http.response import HttpResponse
import requests
from django.shortcuts import render
from .forms import coordinates
from .models import weatherData

def home(request):
    return render(request, 'home.html')

def forcastData(request):
    if request.method== 'POST':

        # getting the input coordinates.
        rawData = coordinates(request.POST)
        print(rawData)
        if rawData.is_valid():
            lat = rawData.cleaned_data['Latitude']
            log = rawData.cleaned_data['Longitude']

            # accessing the api url to get the forcast url for the given coordinates.
            link = "https://api.weather.gov/points/{},{}".format(lat,log)
            response = requests.get(link)
            forcast_link = response.json()['properties']['forecast']

            #requesting server to send forcast details.
            forcast_details = requests.get(forcast_link)
            tempretureDay = forcast_details.json()['properties']['periods'][1]['temperature']
            container = {'temp': tempretureDay,'lat':lat,'log':log}
            obj = weatherData(Latitude=lat, Longitude=log, temperature=tempretureDay)
            obj.save()
            return render(request, 'first.html', container)
        else:
            return HttpResponse("Invalid request", status = 500)
    
    else:
        return HttpResponse("Invalid request", status = 500)