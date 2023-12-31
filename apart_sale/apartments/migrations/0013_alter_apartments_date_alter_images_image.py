# Generated by Django 5.0 on 2023-12-20 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0012_alter_apartments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 11, 0, 18, 292931), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
