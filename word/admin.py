from django.contrib import admin
from word.models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('thai', 'phonetic', 'meaning', 'notes')
    search_fields = ('thai', 'phonetic', 'meaning', 'notes')


admin.site.register(Word, WordAdmin)