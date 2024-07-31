from django.contrib import admin
from bookstore.models import Book


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price')
    list_display_links = ('id', 'title', 'author', 'price')
    search_fields = ('title', 'author')
