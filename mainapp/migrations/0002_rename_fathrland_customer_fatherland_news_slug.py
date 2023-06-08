# Generated by Django 4.1 on 2022-10-23 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fathrland',
            new_name='fatherland',
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]