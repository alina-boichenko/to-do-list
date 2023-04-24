from django.urls import path

from to_do.views import TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list")
]

app_name = "to_do"
