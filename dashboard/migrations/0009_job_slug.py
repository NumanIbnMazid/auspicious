# Generated by Django 3.2 on 2021-06-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210603_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='test', unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
    ]