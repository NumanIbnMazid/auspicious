# Generated by Django 3.2 on 2021-06-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_career_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='url'),
        ),
    ]
