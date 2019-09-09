from django.contrib.gis import admin
from .models import *

admin.site.register(CongressionalDistricts, admin.GeoModelAdmin)
admin.site.register(States, admin.GeoModelAdmin)
# Register your models here.
