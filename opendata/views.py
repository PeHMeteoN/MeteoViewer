from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import phd_bo_d

def index(request):
    params = {}
    return render(request, 'index.html', params)

def list_geocodes(request):
    geocodes = phd_bo_d.geocode.all()
    params = {'geocodes': geocodes}
    return render(request, 'list_geocodes.html', params)
