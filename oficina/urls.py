from django.urls import path
from oficina.views import index, agenda,login_view,remover_do_banco_de_dados,lista_de_clientes, em_servico, adicionar_em_servico, remover_em_servico,novo_cliente,editar_cliente

urlpatterns = [
        path('', index),
        path('agenda/<str:nome_da_oficina>',agenda,name='agenda'),
        path('login/',login_view,name='login'),
        path('remover/<str:nome_da_oficina>/<int:cliente_id>/<str:chave>',remover_do_banco_de_dados,name='remover_do_banco_de_dados'),
        path('lista_de_clientes/<str:nome_da_oficina>/<str:chave>',lista_de_clientes,name='lista_de_clientes'),
        path('veiculos_em_servico/<str:nome_da_oficina>/<str:chave>',em_servico,name='em_servico'),
        path('adicionar_em_servico/<str:nome_da_oficina>/<int:cliente_id>/<str:chave>', adicionar_em_servico, name='adicionar_em_servico'),
        path('remover_em_servico/<str:nome_da_oficina>/<str:cliente_id>/<str:chave>', remover_em_servico, name='remover_em_servico'),
	path('novo_cliente/<str:nome_da_oficina>/<str:chave>',novo_cliente,name='novo_cliente'),
	path('editar_cliente/<str:nome_da_oficina>/<int:cliente_id>/<str:chave>',editar_cliente, name='editar_cliente')
]
