# Generated by Django 3.2 on 2021-06-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_jobposition_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]
