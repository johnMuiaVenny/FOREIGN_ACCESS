from django.urls import path
from .views import *
from . import views

app_name='SocialAccounts'

urlpatterns = [
    path('', SocialMedia, name='SocialMedia'),
]