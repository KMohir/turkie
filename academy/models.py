from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
import os

def news_image_upload_to(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'news/{instance.id}_{base_filename}{file_extension}'

class News(models.Model):
    # Поля для узбекского языка
    title_uz = models.CharField(max_length=200, verbose_name="Заголовок (узбекский)")
    short_description_uz = models.CharField(max_length=300, verbose_name="Краткое описание (узбекский)")
    content_uz = models.TextField(verbose_name="Содержание (узбекский)")

    # Поля для русского языка
    title_ru = models.CharField(max_length=200, verbose_name="Заголовок (русский)")
    short_description_ru = models.CharField(max_length=300, verbose_name="Краткое описание (русский)")
    content_ru = models.TextField(verbose_name="Содержание (русский)")

    # Общие поля
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    image = models.ImageField(upload_to=news_image_upload_to, null=True, blank=True, verbose_name="Изображение")
    published_date = models.DateField(default=now, verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адрес")

    def save(self, *args, **kwargs):
        if not self.slug:
            # Используем title_uz для создания slug, так как это основной язык
            self.slug = slugify(self.title_uz)
        if not self.id:
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # Имя отправителя
    email = models.EmailField()  # Email отправителя
    phone = models.CharField(max_length=20, blank=True)  # Телефон (необязательно)
    message = models.TextField()  # Сообщение
    created_at = models.DateTimeField(auto_now_add=True)  # Дата отправки
    is_processed = models.BooleanField(default=False)  # Обработано ли сообщение

    def __str__(self):
        return f"{self.name} - {self.email}"