from django.shortcuts import render
from library.models import Genre, Movie

def index(request):
    num_movies = Movie.objects.all().count()
    movies = Movie.objects.all()

    context = {
        'num_movies': num_movies,
        'movies': movies
    }

    return render(request, 'index.html', context=context)

def movie(request, id):
    return render(request, 'movie.html', context={'movie': Movie.objects.get(pk = id)})

def search(request):
    q = request.GET.get('q')
    y = request.GET.get('y')
    num_movies = Movie.objects.filter(name__contains=q).filter(year=y).count()
    movies = Movie.objects.filter(name__contains=q).filter(year=y)

    context = {
        'num_movies': num_movies,
        'movies': movies
    }

    return render(request, 'search.html', context=context)