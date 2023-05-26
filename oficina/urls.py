from django.urls import path
from oficina.views import index, agenda,login_view,verificar,lista_de_clientes, em_servico

urlpatterns = [
        path('', index),
        path('agenda/',agenda,name='agenda'),
        path('login/',login_view,name='login'),
        path('verificar/',verificar,name='verificar'),
        path('lista_de_clientes/',lista_de_clientes,name='lista_de_clientes'),
        path('veiculos_em_servico/',em_servico,name='em_servico')

]
