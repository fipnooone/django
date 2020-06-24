from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='images/default.png')
    genre = models.ManyToManyField(Genre)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         return reverse('movie-p', args=[str(self.id)])