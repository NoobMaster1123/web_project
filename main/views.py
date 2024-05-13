from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

import categories
from categories.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'gjljag fjljggj jfljig-4i94jigdfoijggffgfoifsgjghip'
    }

    return render(request, 'main/about.html', context)