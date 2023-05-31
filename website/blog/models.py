from django.db import models
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
static_storage = FileSystemStorage(location=os.path.join(BASE_DIR, 'blog'))


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(
        blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(
        default=True, verbose_name="Публикация")
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name="Категории")
    pdf_file = models.FileField(upload_to="static/blog/pdfs/", verbose_name="PDF-файл", blank=True, storage=static_storage)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Suggestion(models.Model):
    content = models.TextField(
        blank=True, verbose_name="Текст предложения")
    
    def __str__(self):
        return self.content[:30]

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
        ordering = ['id']



class Reception(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=25, verbose_name="Номер телефона")
    question = models.TextField(verbose_name="Вопрос")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Интернет-Приемная'
        ordering = ['id']