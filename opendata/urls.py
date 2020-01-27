from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .models import phd_bo_d
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^list_geocodes/$', views.list_geocodes, name='list_geocodes')
]
