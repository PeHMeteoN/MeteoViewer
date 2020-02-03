from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^app/', include('opendata.urls')),
    url(r'^dash/', include('dashboard.urls')),
    url(r'^/', include('dashboard.urls')),
]
