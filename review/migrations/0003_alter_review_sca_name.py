# Generated by Django 4.2.1 on 2023-05-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_sca_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='sca_name',
            field=models.CharField(max_length=30, verbose_name='스터디카페'),
        ),
    ]
