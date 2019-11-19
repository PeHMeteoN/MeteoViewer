from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .models import OpendataHistoric

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$',GeoJSONLayerView.as_view(model=OpendataHistoric, properties=('cod', 'estado', 'nom')), name='data')

]

urlpatterns += staticfiles_urlpatterns()
