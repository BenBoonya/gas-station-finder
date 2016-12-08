from django.contrib.gis import admin
from .models import gas_station

admin.site.register(gas_station, admin.OSMGeoAdmin)
