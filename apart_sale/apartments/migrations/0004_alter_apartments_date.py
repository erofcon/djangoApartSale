# Generated by Django 5.0 on 2023-12-19 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_rename_apartmentimages_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 17, 42, 26, 104018), verbose_name='Дата публикации'),
        ),
    ]
