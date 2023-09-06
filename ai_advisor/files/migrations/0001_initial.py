# Generated by Django 4.2.4 on 2023-09-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
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
                ("title", models.CharField(max_length=200)),
                ("uploadedFile", models.FileField(upload_to="Uploaded files/")),
                ("dateTimeOfUpload", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
