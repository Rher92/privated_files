from django.contrib import admin
from .models import Files

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    pass