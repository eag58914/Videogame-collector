from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render('home.html')


def about(request):
    return render(request, 'about.html')


def videogames_index(request):
    return render(request, 'videogames/index.html', {'videogames': videogames})
