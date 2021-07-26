from django.urls import path
from .views import *
from . import views

app_name = 'DATABASEmODELS'

urlpatterns = [
    path('', Home, name='Home'),
    path('<int:id>', Song, name='Song'),
    path('Selected', Selected, name='Selected'),
]
