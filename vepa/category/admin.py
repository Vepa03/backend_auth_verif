from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']
    list_editable = ['name']

admin.site.register(Category, CategoryAdmin)
