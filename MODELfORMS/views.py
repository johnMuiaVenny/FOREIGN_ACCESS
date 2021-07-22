from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def Form(request):
    form = Myform()
    if request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Data Saved. Thankyou.</h1>")
    return render(request, 'MODELfORMS/Form.html', {'form':form})
