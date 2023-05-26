from django.contrib import admin
from oficina.models import Cliente

class ListandoClientes(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 10
admin.site.register(Cliente, ListandoClientes)
# Register your models here.
