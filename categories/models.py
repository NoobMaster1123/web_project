from django.db import models


class Categories(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

class Movie(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    grade = models.DecimalField(default=0.0, max_digits=3, decimal_places=2, verbose_name='Оценка')
    imge = models.ImageField(upload_to='categories_images', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'content'
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
    
    def __str__(self):
        return self.name