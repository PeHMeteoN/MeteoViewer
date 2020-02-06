from django.urls import path, re_path
from page import views

urlpatterns = [
    re_path(r'^.*\.html', views.page_html, name='page'),
    path('', views.index, name='index'),
]
