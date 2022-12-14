from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_pub = models.BooleanField(default=True, verbose_name='Опубликирована')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория',
                                 related_name='get_news')
    views_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse(viewname='view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
