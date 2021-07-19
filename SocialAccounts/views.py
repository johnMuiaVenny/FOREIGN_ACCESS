from django.shortcuts import render
from django.http import HttpResponse
from .models import SOCIALaCCOUNTS

# Create your views here.

def SocialMedia(request):
    Accountes = SOCIALaCCOUNTS.objects.order_by('-pk')[:1]
    return render(request, 'SocialAccounts/SocialMedia.html', {'Accountes':Accountes})


