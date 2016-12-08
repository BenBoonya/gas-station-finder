from django.db import models

# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class samplemap(models.Model):
    id = models.IntegerField(primary_key=True)
    name_th = models.CharField(max_length=254)
    name_en = models.CharField(max_length=254)
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPointField(srid=2180)

# Auto-generated `LayerMapping` dictionary for samplemap model
samplemap_mapping = {
    'id' : 'id',
    'name_th' : 'name_th',
    'name_en' : 'name_en',
    'lon' : 'lon',
    'lat' : 'lat',
    'geom' : 'MULTIPOINT',
}
