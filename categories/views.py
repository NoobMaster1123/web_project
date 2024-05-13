from django.shortcuts import render

from categories.models import Movie

def catalog(request):

    categories = Movie.objects.all()
    
    context = {
        'title': 'Home - Каталог',
        'categories': categories
    }
    return render(request, 'categories/catalog.html', context)


def movie(request):
    return render(request, 'categories/movie.html')