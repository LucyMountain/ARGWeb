from django.urls import path

from . import views

app_name = 'puzzle2'
urlpatterns = [
    path('4675726e616365/', views.index, name='index'),
    path('incorrect/', views.fail, name='fail'),
    path('test/', views.test, name='test'),
    path('answer/', views.answer, name='answer'),
    path('hmm/', views.success, name='success'),
]