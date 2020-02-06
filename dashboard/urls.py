from django.urls import path, re_path
from dashboard import views

urlpatterns = [
    re_path(r'^.*\.html', views.visor_html, name='visor'),
    path('', views.index, name='index'),
]
