# Generated by Django 3.2 on 2021-07-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_auto_20210701_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='remarks'),
        ),
    ]