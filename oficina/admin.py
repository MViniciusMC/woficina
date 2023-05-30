from django.contrib import admin
from oficina.models import Cliente, CadastroOficina
class ListandoClientes(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 10

# Register your models here.
class ListandoLogin (admin.ModelAdmin):
    list_display = ( "oficina","chave")
    list_display_links = ("oficina",)
    search_fields = ("oficina",)
    list_per_page = 10
admin.site.register(Cliente, ListandoClientes)
admin.site.register(CadastroOficina, ListandoLogin)
