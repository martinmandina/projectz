# Generated by Django 3.1.3 on 2020-11-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0003_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Id_profile',
            field=models.IntegerField(default=0),
        ),
    ]
