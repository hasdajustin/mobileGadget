from django.contrib import admin
from .models import AudioGear, Charger, Phonecases

# Register your models here.
@admin.register(AudioGear)
class AudioGearAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Charger)
class ChargerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Phonecases)
class PhonecasesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}