from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'schedule', 'moderator','types')
    # search_fields = ('name', 'tagline', 'moderator')

admin.site.register(Event, EventAdmin)
