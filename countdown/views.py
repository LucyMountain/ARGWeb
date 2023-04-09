from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime


def index(request):
    return render(request, 'countdown/counter.html')
