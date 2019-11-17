from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .models import City


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
]

urlpatterns += staticfiles_urlpatterns()