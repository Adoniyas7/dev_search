# Generated by Django 4.2.2 on 2023-06-07 07:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="project",
            name="featured_img",
            field=models.ImageField(upload_to="project_img"),
        ),
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.ManyToManyField(blank=True, to="projects.tag"),
        ),
    ]
