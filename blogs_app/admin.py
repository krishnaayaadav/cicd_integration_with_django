from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug')

    

# admin.site.register(Post)