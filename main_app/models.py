from django.db import models
from django.urls import resolvers, reverse
# Create your models here.
CONSOLE = [
    ('SG', 'Sega Genesis'),
    ('N', 'Nintendo 64'),
    ('GC', 'Game Cube'),
    ('W', 'Wii'),
    ('SW', 'Switch'),
    ('PS', 'Playstation 2'),
    ('PS3', 'Playstation 3'),
    ('PS4', 'Playstation 4'),
    ('X', 'Xbox'),
    ('X1', 'XboxOne')
]


class Console(models.Model):
    console = models.CharField(
        max_length=1,
        choices=CONSOLE,
        default=CONSOLE[0][0]
    )


class Videogames(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    year_release = models.IntegerField()
    console = models.ManyToManyField(Console)

    def __str__(self):
        return self.name


def get_absolute_url(self):
    return reverse('detail', kwargs={'videogame_id': self.id})
