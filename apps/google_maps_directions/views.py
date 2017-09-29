# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
import requests

def index(request):
    return render(request, "google_maps_directions/index.html")
def directions(request):
    if request.method == "POST":
        print request.POST
        origin = request.POST['origin'].replace(' ', '+')
        destination = request.POST['destination'].replace(' ', '+')
        url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&key=<<APIKEY>>"
        response = requests.get(url).content
        print response
        return HttpResponse(response, content_type='application/json')