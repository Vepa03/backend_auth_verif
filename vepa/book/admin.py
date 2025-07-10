from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'description' , 'image', 'category', 'book', 'author']
    list_editable = ['title', 'description' , 'image', 'category', 'book', 'author']

admin.site.register(Book, BookAdmin)
