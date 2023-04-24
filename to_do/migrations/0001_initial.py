# Generated by Django 4.2 on 2023-04-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("deadline_date", models.DateTimeField(blank=True, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="tags", to="to_do.tag"
                    ),
                ),
            ],
            options={
                "ordering": ["status", "-created_date"],
            },
        ),
    ]
