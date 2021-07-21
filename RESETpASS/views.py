from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.contrib.auth.models import User


def Home(request):
	return render(request, 'RESETpASS/password/Home.html')