from django.shortcuts import render
from django.template import context

from categories.models import Movie

def catalog(request):

    categori = Movie.objects.all()
    
    context = {
        'title': 'Home - Каталог',
        'categori': categori
    }
    return render(request, 'categories/catalog.html', context)


def movie(request, movie_slug):

    movie= Movie.objects.get(slug=movie_slug)

    context = {
        'movie': movie
    }
    return render(request, 'categories/movie.html', context=context)