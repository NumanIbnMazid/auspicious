# Generated by Django 3.2 on 2021-05-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_category', to='dashboard.projectcategory', verbose_name='project category'),
        ),
    ]
