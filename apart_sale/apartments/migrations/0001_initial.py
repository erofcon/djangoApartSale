# Generated by Django 5.0 on 2023-12-19 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Описание')),
                ('bedrooms', models.IntegerField(verbose_name='Колличество комнат')),
                ('square_ft', models.IntegerField(verbose_name='Сколько квадратных метров')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('favorite', models.BooleanField(default=False, verbose_name='Добавить в избранные')),
                ('status', models.CharField(choices=[('for_sale', 'на продаже'), ('sales', 'продано')], default='for_sale', max_length=50, verbose_name='Статус')),
                ('images', models.ImageField(upload_to='uploads/', verbose_name='Изображение')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 12, 19, 16, 16, 41, 486275), verbose_name='Дата публикации')),
            ],
        ),
    ]
