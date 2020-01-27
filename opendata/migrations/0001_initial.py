# Generated by Django 2.2 on 2020-01-20 06:37

import django.contrib.gis.db.models.fields as geomodels
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phd_bo_d',
            fields=[
                ('geocode', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('type_station', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('first_year', models.TextField(blank=True, null=True)),
                ('last_year', models.TextField(blank=True, null=True)),
                ('geom', geomodels.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'phd_bo_d',
                'managed': False,
            },
        ),
    ]
