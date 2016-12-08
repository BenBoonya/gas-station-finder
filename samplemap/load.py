import os
from django.contrib.gis.utils import LayerMapping
from .models import samplemap

samplemap_mapping = {
    'id' : 'id',
    'name_th' : 'name_th',
    'name_en' : 'name_en',
    'lon' : 'lon',
    'lat' : 'lat',
    'geom' : 'MULTIPOINT',
}


samplemap_shp = os.path.abspath('hospital.shp')


def run(verbose=True):
    lm = LayerMapping(
        samplemap, samplemap_shp, samplemap_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
