from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Videogames


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def videogames_index(request):
    videogames = Videogames.objects.all()
    return render(request, 'videogames/index.html', {'videogames': videogames})


def videogames_detail(request, videogame_id):
    videogame = Videogames.objects.get(id=videogame_id)
    return render(request, 'videogames/detail.html', {'videogame': videogame})


class VideogameCreate(CreateView):
    model = Videogames
    fields = '__all__'
    success_url = '/videogames/'


class VideogameUpdate(UpdateView):
    model = Videogames
    fields = '__all__'
    success_url = '/videogames/'


class VideogameDelete(DeleteView):
    model = Videogames
    success_url = '/videogames/'
