from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    all_albums=Album.object.all()
    html=''
    for i album in all_albums:
	url='/music/'+ str(album_id)+'/'
    return HttpResponse(html)
def detail(request,album_id):
    return HttpResponse("<h2>details for album id "+str(album_id)+"</h2>")
