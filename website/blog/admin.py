from django.contrib import admin
from . import models
from django.db.models import TextField
from markdownx.widgets import AdminMarkdownxWidget


class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        TextField: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
