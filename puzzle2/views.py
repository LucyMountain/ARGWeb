import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index(request):
    letters = 'WATERMELON'
    for i in range(100):
        letters = letters + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letters = "RKLJQHRTGUGOWFGGRXZVNPDJZESOAOFBFJPBEODQTSYLHXNNHUVPLEGCEONQEZBMWCVUFZNUACBWUEIYPGXPBICFYFSBNRUAKUVYMSAZCHREUUOYKJFXFLIM"
    context = {
        'letters': letters,
    }
    return render(request, 'puzzle2/index.html', context)


def fail(request):
    return render(request, 'puzzle2/fail.html')


def test(request):
    return render(request, 'puzzle2/test.html')


def answer(request):
    if "furnace" == request.POST['text_input'].lower():
        return HttpResponseRedirect(reverse('puzzle2:success'))
    else:
        return HttpResponseRedirect(reverse('puzzle2:fail'))


def success(request):
    return render(request, 'puzzle2/qr.html')
