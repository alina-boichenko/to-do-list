from django.urls import path

from to_do.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks-create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "to_do"
