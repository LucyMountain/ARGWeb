from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime


def index(request):
    first_time = datetime.datetime.now()
    later_time = datetime.datetime(2023, 4, 10, 14, 2, 3)
    difference = (later_time - first_time).total_seconds()
    days = divmod(difference, 86400)  # Get days (without [0]!)
    hours = divmod(days[1], 3600)  # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)  # Use remainder of hours to calc minutes
    seconds = divmod(minutes[1], 1)
    difference = later_time - first_time
    context = {
        'counter': difference,
    }
    return render(request, 'countdown/index.html', context)