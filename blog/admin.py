from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_date", "published_date")
    list_filter = ("created_date", "published_date", "author")
    search_fields = ("title", "text")
    ordering = ("-created_date",)
