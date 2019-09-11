from django.db import models
from django.urls import resolvers, reverse
# Create your models here.


class Videogames(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    year_release = models.IntegerField()

    def __str__(self):
        return self.name


def get_absolute_url(self):
    return reverse('detail', kwargs={'videogame_id': self.id})
