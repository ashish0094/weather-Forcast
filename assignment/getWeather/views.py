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
        if rawData.is_valid():
            lat = rawData.cleaned_data['Latitude']
            log = rawData.cleaned_data['Longitude']

            # accessing the api url to get the forcast url for the given coordinates.
            link = "https://api.weather.gov/points/{},{}".format(lat,log)
            response = requests.get(link)

            # validating whether coordinates are of USA or not.
            if 'status' in response.json() and response.json()['status'] == 404:
                return render(request, 'second.html')

            forcast_link = response.json()['properties']['forecast']

            #requesting server to send forcast details.
            forcast_details = requests.get(forcast_link)
            print(forcast_details.json().keys())
            tempretureDay = forcast_details.json()['properties']['periods'][1]['temperature']
            container = {'temp': tempretureDay,'lat':lat,'log':log}
            obj = weatherData(Latitude=lat, Longitude=log, temperature=tempretureDay)
            obj.save()
            return render(request, 'first.html', container)
        else:
            return HttpResponse("Invalid request", status = 500)