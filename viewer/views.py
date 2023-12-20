from logging import getLogger

from django.shortcuts import render

# Create your views here.

LOGGER = getLogger()


def index(request):
    return render(request, 'index.html')
