from django.views.generic import CreateView

# Create your views here.
from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'tasks/task_form.html'
