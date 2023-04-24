from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from to_do.models import Task, Tag


class TaskForms(forms.ModelForm):
    content = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Write your task..."})
    )
    deadline_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now().strftime('%Y-%m-%dT%H:%M'),
        required=False
    )
    status = forms.BooleanField(label="Done", required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def clean_deadline_date(self):
        deadline_date = self.cleaned_data["deadline_date"]
        if deadline_date < timezone.now():
            raise ValidationError(
                "The deadline date must be after the created date"
            )
        return deadline_date

    class Meta:
        model = Task
        fields = ("content", "deadline_date", "status", "tags")
