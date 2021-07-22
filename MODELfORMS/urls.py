from django.urls import path
from .views import *
from . import views

app_name = 'MODELfORMS'

urlpatterns = [
    path('', Form, name='Form'),
]