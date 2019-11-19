from django.contrib.gis.db import models

class OpendataHistoric(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    cate = models.TextField(blank=True, null=True)
    cod = models.TextField(blank=True, null=True)
    cod_old = models.FloatField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    ico = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opendata_historic'
