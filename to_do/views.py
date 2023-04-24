from django.shortcuts import render
from django.views.generic import ListView

from to_do.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "to_do/task_list.html"


class TagListView(ListView):
    model = Tag
    template_name = "to_do/tag_list.html"
