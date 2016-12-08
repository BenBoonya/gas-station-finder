import os
from django.contrib.gis.utils import LayerMapping
from .models import gas_station

gas_station_mapping = {
    'name' : 'name',
    'lon' : 'lon',
    'lat' : 'lat',
    'geom' : 'MULTIPOINT',
}

gas_station_shp = os.path.abspath(os.path.join('data','gas_stations', 'gas_stations.shp'))

def run(verbose=True):
    lm = LayerMapping(gas_station, gas_station_shp, gas_station_mapping,
                      transform=False, encoding='utf8')

    lm.save(strict=True, verbose=verbose)
