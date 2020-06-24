from django.contrib import admin
from .models import Movie
from .models import Genre

admin.site.register(Movie)
admin.site.register(Genre)