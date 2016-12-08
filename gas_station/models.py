from django.db import models

# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible
class gas_station(models.Model):
    name = models.CharField(max_length=254)
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPointField(srid=2180)

    def __str__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for gas_station model
gas_station_mapping = {
    'name' : 'name',
    'lon' : 'lon',
    'lat' : 'lat',
    'geom' : 'MULTIPOINT',
}
