# Generated by Django 4.2 on 2023-05-31 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_placeofwork_created_placeofwork_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='topic',
        ),
    ]
