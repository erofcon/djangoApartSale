from datetime import datetime

from django.db import models

STATUS_CHOICES = (
    ("for_sale", "на продаже"),
    ("sales", "продано"),
)


class Apartments(models.Model):
    title = models.CharField('Название', max_length=250)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Описание')
    price = models.IntegerField('Цена', default=0)
    bedrooms = models.IntegerField('Колличество комнат')
    square_ft = models.IntegerField('Сколько квадратных метров')
    address = models.CharField('Адрес', max_length=250)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    favorite = models.BooleanField('Добавить в избранные', default=False)
    status = models.CharField('Статус', choices=STATUS_CHOICES, max_length=50, default='for_sale')
    plan = models.ImageField('Планировка', upload_to='upload_images/', blank=True)
    show = models.BooleanField('Показывать на сайте', default=True)
    date = models.DateTimeField('Дата публикации', default=datetime.now())

    def __str__(self):
        return self.title

    def first_image(self):
        return self.images.first()

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'


class Images(models.Model):
    apartment = models.ForeignKey(Apartments, default=None, on_delete=models.CASCADE, related_name="images", )
    image = models.ImageField('Изображение', upload_to='upload_images/', blank=True)

    def __str__(self):
        return self.apartment.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение'
