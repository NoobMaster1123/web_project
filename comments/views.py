from django.shortcuts import render
from comments.models import Task

def comment(request):
    tasks = Task.objects.all()
    return render(request, 'comments/comments.html', {'title': 'Homesite', 'tasks': tasks})

