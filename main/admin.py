from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'pub_date']
    list_filter = ['author', 'category', 'pub_date']
    search_fields = ['title', 'body']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']