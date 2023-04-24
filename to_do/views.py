from django.shortcuts import render
from django.views.generic import ListView

from to_do.models import Task


class TaskListView(ListView):
    model = Task
    template_name = "to_do/task_list.html"
