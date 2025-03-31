from django.contrib import admin
from .models import News
from django.utils.translation import get_language

class NewsAdmin(admin.ModelAdmin):
    # Отображаем поля в списке новостей
    list_display = ('get_title', 'published_date', 'views_count')
    list_filter = ('published_date',)
    search_fields = ('title_uz', 'title_ru', 'short_description_uz', 'short_description_ru')
    prepopulated_fields = {'slug': ('title_uz',)}  # Используем title_uz для slug
    fieldsets = (
        ('Узбекский', {
            'fields': ('title_uz', 'short_description_uz', 'content_uz')
        }),
        ('Русский', {
            'fields': ('title_ru', 'short_description_ru', 'content_ru')
        }),
        ('Общие данные', {
            'fields': ('slug', 'image', 'published_date', 'address')
        }),
    )

    # Метод для отображения заголовка в зависимости от текущего языка
    def get_title(self, obj):
        current_language = get_language()
        if current_language == 'ru':
            return obj.title_ru
        return obj.title_uz

    get_title.short_description = 'Заголовок'  # Название столбца в админке

admin.site.register(News, NewsAdmin)