from django.shortcuts import render


def catalog(request):
    return render(request, 'categories/catalog.html')


def movie(request):
    return render(request, 'categories/movie.html')