from django.test import TestCase
from django.utils import timezone

from to_do.forms import TaskForms
from to_do.models import Tag, Task


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test tag")
        self.task = Task.objects.create(content="Test task")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), self.tag.name)

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.content)


class FormTests(TestCase):
    def test_create_correct_deadline_date(self):
        form_data = {
            "content": "Testing",
            "deadline_date": timezone.now() + timezone.timedelta(days=1)
        }
        form = TaskForms(data=form_data)

        self.assertTrue(form.is_valid())

    def test_create_deadline_date_in_the_past(self):
        form_data = {
            "content": "Testing 2",
            "deadline_date": timezone.now() + timezone.timedelta(days=-3),
        }

        form = TaskForms(data=form_data)
        self.assertFalse(form.is_valid())
