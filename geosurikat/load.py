import os
from django.contrib.gis.utils import LayerMapping
from .models import Toledo

toledo_mapping = {
    'pntnum': 'PntNum',
    'panoid': 'panoID',
    'panodate': 'panoDate',
    'greenview': 'greenView',
    'url0': 'url0',
    'url60': 'url60',
    'url120': 'url120',
    'url180': 'url180',
    'url300': 'url300',
    'url240': 'url240',
    'geom': 'MULTIPOINT25D',
}

toledo_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'toledo.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        data, toledo_shp, toledo_mapping,
        transform=False, encoding='UTF-8',
    )
    lm.save(strict=True, verbose=verbose)

