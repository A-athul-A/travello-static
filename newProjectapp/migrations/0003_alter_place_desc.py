# Generated by Django 4.1.2 on 2022-10-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newProjectapp', '0002_place_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
