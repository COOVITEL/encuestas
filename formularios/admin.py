from django.contrib import admin
from .models import Asociado, Colaborador, Dirigente

@admin.register(Asociado)
class AsociadoAdmin(admin.ModelAdmin):
    list_display = ['name', 'cedula', 'nivelEducativo', 'familiares', 'familiaresDetalles']

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['name', 'cargo', 'años']

@admin.register(Dirigente)
class DirigenteAdmin(admin.ModelAdmin):
    list_display = ['name', 'cargo', 'años']