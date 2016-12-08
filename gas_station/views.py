from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import gas_station
from django.views.generic import TemplateView
import json

def points_view(request):
    points_as_geojson = serialize('geojson', gas_station.objects.all(),indent=3, ensure_ascii=False)

    return HttpResponse(points_as_geojson.encode('utf8'), content_type='json')

class MainPageView(TemplateView):
    template_name = 'gas_station/index.html'
