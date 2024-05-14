from django.shortcuts import render

from categories.models import Movie

def catalog(request):

    categori = Movie.objects.all()
    
    context = {
        'title': 'Home - Каталог',
        'categori': categori
    }
    return render(request, 'categories/catalog.html', context)


def movie(request):
    return render(request, 'categories/movie.html')