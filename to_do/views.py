from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from to_do.forms import TaskForms
from to_do.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "to_do/task_list.html"


class TaskCreateView(CreateView):
    form_class = TaskForms
    template_name = "to_do/task_form.html"
    success_url = reverse_lazy("to_do:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForms
    success_url = reverse_lazy("to_do:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:task-list")


class ChangeTaskStatusView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)

        if task.status is True:
            task.status = False
        else:
            task.status = True
        task.save()

        return HttpResponseRedirect(
            redirect_to=reverse_lazy("to_do:task-list")
        )


class TagListView(ListView):
    model = Tag
    template_name = "to_do/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tag-list")
