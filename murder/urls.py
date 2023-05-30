from django.urls import path

from . import views

app_name = 'murder'
urlpatterns = [
    path('', views.index, name='index'),
]