from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Videogames


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')


def videogames_index(request):
    videogames = Videogames.objects.all()
    return render(request, 'videogames/index.html', {'videogames': videogames})
