from comments import views

from django.urls import path

app_name = 'comments'
urlpatterns = [
     path('comments/', views.comment, name='comments'),
]

