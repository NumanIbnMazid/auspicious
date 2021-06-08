# Generated by Django 3.2 on 2021-06-07 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0015_merge_0013_career_contact_0014_alter_jobposition_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_created_by', to='auth.user', verbose_name='created by'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='career',
            name='file',
            field=models.FileField(upload_to='', verbose_name='file'),
        ),
    ]