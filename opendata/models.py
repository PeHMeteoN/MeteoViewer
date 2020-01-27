from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point

class phd_bo_d(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    geocode = models.TextField(db_column='GEOCODE', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='LON', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    type_station = models.TextField(db_column='TYPE_STATION', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    first_year = models.TextField(db_column='FIRST_YEAR', blank=True, null=True)  # Field name made lowercase.
    last_year = models.TextField(db_column='LAST_YEAR', blank=True, null=True)  # Field name made lowercase.
    geom = models.PointField(db_column='geom', blank=True, null=True, srid=4326)

    def __str__(self):
        return self.geocode

    class Meta:
        managed = False
        db_table = 'phd_bo_d'
