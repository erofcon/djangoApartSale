# Generated by Django 5.0 on 2023-12-20 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0009_alter_apartments_date_alter_apartments_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 10, 46, 51, 626980), verbose_name='Дата публикации'),
        ),
    ]