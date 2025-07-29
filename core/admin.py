from django.contrib import admin
from .models import AudioGear

# Register your models here.
@admin.register(AudioGear)
class AudioGearAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}