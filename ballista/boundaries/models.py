from django.contrib.gis.db import models

class States(models.Model):
    region = models.CharField(max_length=2)
    division = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, unique=True)
    statens = models.CharField(max_length=8)
    geoid = models.CharField(max_length=2)
    stusps = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for States model
states_mapping = {
    'region': 'REGION',
    'division': 'DIVISION',
    'statefp': 'STATEFP',
    'statens': 'STATENS',
    'geoid': 'GEOID',
    'stusps': 'STUSPS',
    'name': 'NAME',
    'lsad': 'LSAD',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}

class CongressionalDistricts(models.Model):
    statefp = models.ForeignKey(States, to_field='statefp', on_delete=models.DO_NOTHING)
    cd116fp = models.CharField(max_length=2)
    geoid = models.CharField(max_length=4)
    namelsad = models.CharField(max_length=41)
    lsad = models.CharField(max_length=2)
    cdsessn = models.CharField(max_length=3)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for CongressionalDistricts model
congressionaldistricts_mapping = {
    'statefp': 'STATEFP',
    'cd116fp': 'CD116FP',
    'geoid': 'GEOID',
    'namelsad': 'NAMELSAD',
    'lsad': 'LSAD',
    'cdsessn': 'CDSESSN',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}