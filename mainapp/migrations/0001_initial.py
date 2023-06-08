# Generated by Django 4.1 on 2022-10-19 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('topic', models.CharField(max_length=255, verbose_name='Тақырыбы')),
                ('message', models.TextField(max_length=5000, verbose_name='Хабарлама')),
                ('completed', models.BooleanField(default=False, verbose_name='Орындалды')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Кеңес алушы',
                'verbose_name_plural': 'Кеңес алушылар',
                'db_table': 'consultations',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Аты')),
                ('fathrland', models.CharField(blank=True, max_length=255, null=True, verbose_name='Әкесінің')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тегі')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('jsn', models.CharField(blank=True, max_length=12, null=True, verbose_name='ЖСН')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Туылған күні')),
                ('education', models.CharField(blank=True, max_length=255, null=True, verbose_name='Білімі')),
                ('profession', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кәсіби мамандығы')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Қолданушы',
                'verbose_name_plural': 'Қолданушылар',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тақырыбы')),
                ('description', models.TextField(max_length=5000, verbose_name='Сипаттамасы')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Сурет')),
                ('data_created', models.DateTimeField(auto_now_add=True, verbose_name='Күні')),
            ],
            options={
                'verbose_name': 'Жаңалық',
                'verbose_name_plural': 'Жаңалықтар',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_work', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Наградтаулар және көтермелеулер')),
                ('data_created', models.DateField(blank=True, null=True, verbose_name='Датасы')),
                ('command', models.CharField(blank=True, max_length=255, null=True, verbose_name='Құжат,датасы')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Қолданушы')),
            ],
            options={
                'verbose_name': 'Наградтау және көтермелеу',
                'verbose_name_plural': 'Наградтаулар және көтермелеулер',
                'db_table': 'rewards',
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_work', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Жұмыс орын')),
                ('data_created', models.DateField(blank=True, null=True, verbose_name='Жұмысқа тұрған уақыты')),
                ('data_ended', models.DateField(blank=True, null=True, verbose_name='Жұмыстан шыққан уақыты')),
                ('command', models.CharField(blank=True, max_length=255, null=True, verbose_name='Құжат,датасы')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Қолданушы')),
            ],
            options={
                'verbose_name': 'Еңбек кітапша',
                'verbose_name_plural': 'Еңбек кітапша',
                'db_table': 'employments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Аты')),
                ('last_name', models.CharField(max_length=255, verbose_name='Тегі')),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='Почта')),
                ('staff', models.BooleanField(default=False, verbose_name='Қызметкер')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Қызметкер',
                'verbose_name_plural': 'Қызметкерлер',
                'db_table': 'employees',
            },
        ),
    ]
