# Generated by Django 4.1 on 2023-01-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_employment_file_delete_employmentfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл'),
        ),
    ]
