# Generated by Django 4.2 on 2023-05-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=64)),
                ("useremail", models.EmailField(max_length=64)),
                ("password", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "카페앱 사용자",
                "verbose_name_plural": "카페앱 사용자",
                "db_table": "cafeProject_user",
            },
        ),
    ]