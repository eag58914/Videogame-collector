from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('videogames/', views.videogames_index, name='index'),
    path('videogames/<int:videogame_id>/',
         views.videogames_detail, name='detail'),
    path('videogames/create/', views.VideogameCreate.as_view(),
         name='videogame_create'),
    path('videogames/<int:pk>/update/',
         views.VideogameUpdate.as_view(), name='videogame_update'),
    path('videogames/<int:pk>/delete/',
         views.VideogameDelete.as_view(), name='videogame_delete'),
]
