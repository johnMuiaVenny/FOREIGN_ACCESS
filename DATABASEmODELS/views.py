from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.

def Home(request):
    try:
        singer = SINGER.objects.all()
    except SINGER.DoesNotExist:
        singer = 'Singer Not Found!!'
        return render(request, 'DATABASEmODELS/Home.html', {'singer':singer})
    return render(request, 'DATABASEmODELS/Home.html', {'singer':singer})



#Get songs of an individual singer.
def Song(request, id):

    Singer = get_object_or_404(SINGER, pk=id)

    if request.method == 'GET':
        try:
            song = Singer.song_set.all()
        except Singer.DoesNotExist:
            song = 'No Songs For This Singer!!'
            return render(request, 'DATABASEmODELS/Song.html', {'song':song})
        return render(request, 'DATABASEmODELS/Song.html', {'song':song, 'Singer':Singer})


def Selected(request):
    if request.method == 'POST':
        try:
            song = SONG.objects.get(pk=request.POST['song_id'])
            return render(request, 'DATABASEmODELS/Selected.html', {'song':song})
        except(KeyError, SONG.DoesNotExist):
            error = 'No Song Selected!!'
            return render(request, 'DATABASEmODELS/Song.html', {'error':error})