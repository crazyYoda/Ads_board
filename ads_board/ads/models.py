from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# class Author(models.Model):
#     authorUser = models.OneToOneField(User, on_delete=models.CASCADE)


class Ads(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Текст объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    ads_response = models.TextField(verbose_name='Отклик')

    def get_absolute_url(self):
        return reverse('view_ads', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class AdsResponse(models.Model):
    ads_response = models.ForeignKey('Ads', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return self.ads_response