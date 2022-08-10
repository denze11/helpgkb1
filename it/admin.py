from django.contrib import admin
from .models import ItYear


@admin.register(ItYear)
class ItAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'description',)
    list_display_links = ('id', 'department', 'description',)
    list_filter = ('department',)
    search_fields = ('description',)
