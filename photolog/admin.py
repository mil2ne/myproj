from django.contrib import admin

from .models import Photo, Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
