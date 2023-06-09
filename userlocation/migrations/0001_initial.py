# Generated by Django 4.2 on 2023-05-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Userlocation",
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
                ("location", models.CharField(max_length=128)),
            ],
            options={
                "verbose_name": "사용자위치",
                "verbose_name_plural": "사용자위치",
                "db_table": "user_location",
            },
        ),
    ]
