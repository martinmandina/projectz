# Generated by Django 2.1.4 on 2020-11-30 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0002_auto_20201130_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
