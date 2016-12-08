from django.db import models

# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class gas_station(models.Model):
    name = models.CharField(max_length=254)
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPointField(srid=2180)

# Auto-generated `LayerMapping` dictionary for gas_station model
gas_station_mapping = {
    'name' : 'name',
    'lon' : 'lon',
    'lat' : 'lat',
    'geom' : 'MULTIPOINT',
}
