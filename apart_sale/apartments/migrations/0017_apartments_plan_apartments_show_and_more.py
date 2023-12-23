# Generated by Django 5.0 on 2023-12-21 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0016_alter_apartments_date_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='plan',
            field=models.ImageField(blank=True, upload_to='upload_images/', verbose_name='Планировка'),
        ),
        migrations.AddField(
            model_name='apartments',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Показывать на сайте'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 9, 6, 9, 914522), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload_images/', verbose_name='Изображение'),
        ),
    ]