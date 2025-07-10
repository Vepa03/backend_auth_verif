from django.contrib import admin
from .models import Suggestion

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'description', 'book']
    list_editable = ['name', 'description', 'book']

admin.site.register(Suggestion, SuggestionAdmin)
