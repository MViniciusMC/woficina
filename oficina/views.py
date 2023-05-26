from django.shortcuts import render, redirect
from oficina.models import Login, Cliente
from django.contrib.auth import authenticate, login



def index(request):
    return render(request, 'index.html')
def agenda(request):
    return render(request,'agenda.html')
def lista_de_clientes(request):
    cliente = Cliente.objects.all()
    return render(request, 'banco_clientes.html', {'clientes':cliente})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_de_clientes')
        else:
            redirect('login')

    return render(request,'login.html')
def verificar(request):
    return render(request,'verificar.html')
def em_servico(request):
    cliente = Cliente.objects.order_by("id").filter(em_servico=True)
    if request.method == 'POST':
        chassi = request.POST['chassi']
        if chassi != None or chassi != '':
            cliente_filtrado = Cliente.objects.order_by("id").filter(chassi=chassi)      
    else:
        cliente_filtrado = None

    return render(request,'veiculos_em_servico.html', {'clientes':cliente, 'clientes_filtrados':cliente_filtrado})

