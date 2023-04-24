from django.db import models


class Tag(models.Model):
    name = models.TextField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def __str__(self) -> str:
        return self.content

    class Meta:
        ordering = ["status", "-created_date"]
