# Generated by Django 4.1.2 on 2022-10-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newProjectapp', '0003_alter_place_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=250)),
                ('Pimg', models.ImageField(upload_to='person')),
                ('Pdesc', models.TextField()),
            ],
        ),
    ]