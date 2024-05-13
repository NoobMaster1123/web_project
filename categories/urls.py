from django.urls import path

from categories import views

app_name = 'categories'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('movie/',views.movie, name='movie')
]