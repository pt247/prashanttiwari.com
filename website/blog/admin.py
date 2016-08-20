from django.contrib import admin
from . import models
# from django_markdown.admin import MarkdownModelAdmin


class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)
