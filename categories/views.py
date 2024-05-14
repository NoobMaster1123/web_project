from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from categories.models import Movie
from categories.utils import q_search

def catalog(request, category_slug=None):

    page= request.GET.get('page',1)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        categori = Movie.objects.all()
    elif query:
        categori = q_search(query)
    else:
        categori = get_list_or_404(Movie.objects.filter(category__slug=category_slug))
        
    paginator = Paginator(categori, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'categori': current_page,
        'slug_url': category_slug
    }
    return render(request, 'categories/catalog.html', context)


def movie(request, movie_slug):

    movie= Movie.objects.get(slug=movie_slug)

    context = {
        'movie': movie
    }
    return render(request, 'categories/movie.html', context=context)