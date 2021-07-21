from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.


#Changing user password
def user(request):
    if request.method == 'POST':
        Pass1 = request.POST['password1']
        Pass2 = request.POST['password2']
        Username = request.POST['username']

        try:
            user = User.objects.get(username=Username)
        except User.DoesNotExist:
            return HttpResponse("USER NAME DOES NOT EXIST.")
        
        if user is not None:
            user.set_password(Pass1)  #Note....
            user.save()
            return HttpResponse("PASSWORD CHANGED SUCCESSIFULLY.")

    return render(request, 'AUTHENTICATIONaPP/User.html')

