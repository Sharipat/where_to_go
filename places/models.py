from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description_short = models.TextField(max_length=400, verbose_name='Краткое описание')
    description_long = tinymce_models.HTMLField(verbose_name='Полное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Ширина')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    order = models.IntegerField(verbose_name='Порядок')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')

    def __str__(self):
        return f'{self.order} {self.place.title}'