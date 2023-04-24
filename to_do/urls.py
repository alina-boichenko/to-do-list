from django.urls import path

from to_do.views import (
    TaskListView,
    TaskCreateView,
    TagListView,
    TagCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks-create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "to_do"
