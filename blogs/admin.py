from django.contrib import admin

from .models import Blog, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "author", "is_featured", "status")
    search_fields = ("id", "title", "category__category_name", "status")
    list_editable = ("is_featured",)


admin.site.register(Category)
