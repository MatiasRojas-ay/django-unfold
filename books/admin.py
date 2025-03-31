from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad")
    search_fields = ("nombre", "nacionalidad")


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "genero", "fecha_publicacion")
    list_filter = ("genero", "fecha_publicacion")
    search_fields = ("titulo", "autor__nombre")
    date_hierarchy = "fecha_publicacion"