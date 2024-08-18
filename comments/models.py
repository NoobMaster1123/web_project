from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    task = models.TextField('Описание')

    class Meta: 
        verbose_name="Задача"
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
    