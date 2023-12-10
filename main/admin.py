from django.contrib import admin
from .models import Post, Category

# admin.site.register(Post)
admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'pub_date']
    list_filter = ['author', 'category', 'pub_date']
    search_fields = ['title', 'body']
