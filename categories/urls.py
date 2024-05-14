from django.urls import path

from categories import views

app_name = 'categories'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('movie/<slug:movie_slug>/',views.movie, name='movie'),
]