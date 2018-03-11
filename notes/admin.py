from django.contrib import admin
from .models import Note
 
class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note
 
admin.site.register(Note,NoteAdmin)
# Register your models here.
