# Generated by Django 4.1 on 2023-02-16 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0012_placeofwork_alter_employment_command_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeofwork',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Тіркелу уақыты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placeofwork',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='placeofwork',
            name='bin',
            field=models.CharField(max_length=12, verbose_name='БСН'),
        ),
        migrations.AlterField(
            model_name='placeofwork',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Мекеме аты'),
        ),
    ]
