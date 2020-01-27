from leaflet.admin import LeafletGeoAdmin
from . import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.phd_bo_d, LeafletGeoAdmin)