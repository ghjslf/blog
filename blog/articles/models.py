from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, blank=True)
    preview = None
    annotation = models.CharField(verbose_name='Сводка', max_length=255, blank=True)
    content = models.TextField(verbose_name='Содержание', blank=True)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True,)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True,)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Метки')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
