from django.contrib import admin
from .models import Desenvolvedora, Jogo, Plataforma

# Register your models here.
@admin.register(Desenvolvedora)
class DesenvolvedoraAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "pais")
    search_fields = ("nome",)


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "fabricante")
    search_fields = ("nome",)


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "desenvolvedora", "plataforma", "ano_lancamento")
    list_filter = ("desenvolvedora", "plataforma")
    search_fields = ("nome",)