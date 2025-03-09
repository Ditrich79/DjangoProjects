from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']  # Фильтр справа в админке по указанным полям
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение поля слаг
    raw_id_fields = ['author']  # Позволяет найти пользователя по id
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS  # Создаёт в фильтре справа количество объектов


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


