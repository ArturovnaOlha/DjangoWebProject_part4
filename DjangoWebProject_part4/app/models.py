"""
Definition of models.
"""
# new
from tabnanny import verbose
from tkinter import CASCADE
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# end new

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")
    # Методы класса:
    def get_absolute_url(self): # метод возвращает строку с юрл адресом записи
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self): # метод возвращает значение, используемое для представления отдельных записей в админ отделе
        return self.title

# Метаданные - вложенный класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Posts" # имя таблицы для модели
        ordering = ["-posted"] # порядок сортировки данных в модели ("-" по убыванию)
        verbose_name = "статья блога" # имя, под кот-м модель будет отображаться в админ разделе (для 1 статьи блога)
        verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default= datetime.now(), db_index = True, verbose_name="Дата комментария")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name="Статья комментария")

    # методы класса:
    def __str__(self): # вернет название, юзаемое для представления отдельных записей в админ разделе
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)

    # метаданные вложенный класс, задающий доп параметры модели
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарии к статьям блога"
        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)