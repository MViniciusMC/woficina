from django.shortcuts import render, redirect
from oficina.models import CadastroOficina, Cliente
from django.contrib.auth import authenticate, login
import random
from datetime import datetime


def index(request):
    return render(request, 'index.html')
def agenda(request, nome_da_oficina):
    return render(request,'agenda.html',{'nome_da_oficina':nome_da_oficina})
def lista_de_clientes(request, nome_da_oficina,chave):
    chave = request.session.get('chave')
    cliente = Cliente.objects.order_by("id").filter(oficina=nome_da_oficina)
    if request.method == 'POST':
        chassi = request.POST['chassi']
        if chassi:
            cliente = Cliente.objects.order_by("id").filter(chassi=chassi, oficina=nome_da_oficina)
        else:
            cliente = Cliente.objects.order_by("id").filter(oficina=nome_da_oficina)
    
    
    return render(request, 'banco_clientes.html', {'clientes':cliente, 'nome_da_oficina':nome_da_oficina, 'chave':chave})

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        nome_da_oficina = request.POST['nome_oficina']
        chave = request.POST['chave']

        # Verificar se o usuário e senha estão corretos
        user = authenticate(request, username=usuario, password=senha)
        if chave and nome_da_oficina:
        	# Verificar se a oficina existe no banco de dados
        	cliente = CadastroOficina.objects.filter(oficina=nome_da_oficina,chave=chave).exists()

        if user and cliente:
            login(request, user)
            request.session['chave'] = chave
            return redirect('em_servico', nome_da_oficina=nome_da_oficina, chave=chave)
        else:
            return redirect('login')

    return render(request, 'login.html')


    return render(request,'login.html')
def remover_do_banco_de_dados(request, nome_da_oficina,cliente_id,chave):
	cliente = Cliente.objects.get(pk=cliente_id)
	if request.method == 'POST':
	    confirmacao = request.POST.get('confirmacao', False)
	    if cliente and confirmacao:
	        cliente.delete()
	        return redirect('lista_de_clientes', nome_da_oficina=nome_da_oficina, chave=chave)
	return render(request, 'remover_do_banco_de_dados.html',{'nome_da_oficina':nome_da_oficina,'cliente_id':cliente_id,'chave':chave,'cliente':cliente})
def em_servico(request, nome_da_oficina,chave):
    chave = request.session.get('chave')
    if chave:
        cliente = Cliente.objects.order_by("id").filter(em_servico=True, oficina=nome_da_oficina)
        if request.method == 'POST':
            chassi = request.POST['chassi']
            if chassi != None or chassi != '':
                cliente_filtrado = Cliente.objects.order_by("id").filter(chassi=chassi, oficina=nome_da_oficina)
        else:
            cliente_filtrado = None
    else:
        return redirect('login')
    return render(request, 'veiculos_em_servico.html',
                  {'clientes': cliente, 'clientes_filtrados': cliente_filtrado, 'nome_da_oficina': nome_da_oficina, 'chave': chave})

def adicionar_em_servico(request, nome_da_oficina, cliente_id, chave):
    chave = request.session.get('chave')
    if chave:
        if request.method == 'POST':
            cliente = Cliente.objects.get(pk=cliente_id)
            
            servico = request.POST['servico']
            valor_pecas = request.POST['valor_pecas']
            valor_servico = request.POST['valor_servico']
            data_encerramento = request.POST['data_entrega']
            
            cliente.data_inicio = datetime.now
            #verifica valor servico
            if not valor_servico:
                if cliente.valor_servico:
                   valor_servico = cliente.valor_servico
                else:
                   valor_servico = 0
            #verifica valor pecas 
            if not valor_pecas:
                if cliente.valor_pecas:
                   valor_pecas = cliente.valor_pecas
                else:
                   valor_pecas = 0  
            #verifica servico
            if not servico:
                if cliente.servico:
                    servico = cliente.servico
                else:
                    servico = ""
            # Verifica data_encerramento
            if not data_encerramento:
                if cliente.data_encerramento:
                    data_encerramento = cliente.data_encerramento
                else:
                    data_encerramento = datetime.now
            # verifica em serviço
            
                
            
            # Salvando
            cliente.em_servico = True
            cliente.data_encerramento = data_encerramento
            cliente.servico = servico
            cliente.valor_servico = valor_servico
            cliente.valor_pecas = valor_pecas
            cliente.save()
            return redirect('em_servico', nome_da_oficina=nome_da_oficina, chave=chave)

    else:
        return redirect('login')
    return render(request, 'adicionar_em_servico.html')
def remover_em_servico(request,nome_da_oficina,cliente_id,chave):
    cliente = Cliente.objects.get(pk=cliente_id)
    if cliente.em_servico == True:
        cliente.em_servico = False
        cliente.save()
    return redirect('em_servico',nome_da_oficina=nome_da_oficina,chave=chave)
def novo_cliente(request, nome_da_oficina,chave):
    if request.method =='POST':
        nome = request.POST['nome']
        chassi = request.POST['chassi']
        telefone = request.POST['telefone']
        cpf = request.POST['cpf']
        valor_servico = request.POST['valor_servico']
        placa = request.POST['placa']
        valor_pecas = request.POST['valor_pecas']
        data_entrega = request.POST['data_entrega']
        servico = request.POST['servico']
        em_servico = request.POST.get('em_servico', False)
        
        #verifica chassi,telefone e nome
        if not nome or not chassi or not telefone:
            return redirect('novo_cliente',nome_da_oficina=nome_da_oficina,chave=chave)
        #verifica cpf
        if not cpf:
            cpf = 0
        #verifica placa
        if not placa:
            placa = ''
        #verifica valor servico
        if not valor_servico:
            valor_servico = 0
            #verifica valor pecas 
        if not valor_pecas:
            valor_pecas = 0  
        #verifica servico
        if not servico:              
            servico = ""
         # Verifica data_encerramento
        if not data_entrega:
            data_entrega = datetime.now()
        # verifica em serviço
        if em_servico:
            em_servico = True
        else:
            em_servico = False
        cliente = Cliente(
            nome=nome, 
            chassi=chassi, 
            telefone=telefone, 
            cpf=cpf, 
            placa=placa, 
            valor_servico=valor_servico, 
            valor_pecas=valor_pecas,
            data_encerramento=data_entrega,
            servico=servico, 
            em_servico=em_servico, 
            oficina=nome_da_oficina 
        )
        cliente.save()
        return redirect('em_servico', nome_da_oficina=nome_da_oficina,chave=chave)
    else:
        pass
    return render(request,'novo_cliente.html',{'nome_da_oficina':nome_da_oficina,'chave':chave})
def editar_cliente(request, nome_da_oficina,cliente_id,chave):
    if chave:
        if request.method == 'POST':
            cliente = Cliente.objects.get(pk=cliente_id)
            nome = request.POST['nome']
            chassi = request.POST['chassi']
            telefone = request.POST['telefone']
            cpf = request.POST['cpf']
            valor_servico = request.POST['valor_servico']
            placa = request.POST['placa']
            valor_pecas = request.POST['valor_pecas']
            data_entrega = request.POST['data_entrega']
            servico = request.POST['servico']
            em_servico = request.POST.get('em_servico', False)
            
            # Verifica nome
            if not nome:
                if cliente.nome:
                    nome = cliente.nome
                else:
                    nome = ""
            
            # Verifica chassi
            if not chassi:
                if cliente.chassi:
                    chassi = cliente.chassi
                else:
                    chassi = ""
            
            # Verifica telefone
            if not telefone:
                if cliente.telefone:
                    telefone = cliente.telefone
                else:
                    telefone = ""
            
            # Verifica CPF
            if not cpf:
                if cliente.cpf:
                    cpf = cliente.cpf
                else:
                    cpf = ""
            
            # Verifica placa
            if not placa:
                if cliente.placa:
                    placa = cliente.placa
                else:
                    placa = ""
            
            # Verifica valor do serviço
            if not valor_servico:
                if cliente.valor_servico:
                    valor_servico = cliente.valor_servico
                else:
                    valor_servico = 0
            
            # Verifica valor das peças
            if not valor_pecas:
                if cliente.valor_pecas:
                    valor_pecas = cliente.valor_pecas
                else:
                    valor_pecas = 0
            
            # Verifica serviço
            if not servico:
                if cliente.servico:
                    servico = cliente.servico
                else:
                    servico = ""
            
            # Verifica data de encerramento
            if not data_entrega:
                if cliente.data_encerramento:
                    data_entrega = cliente.data_encerramento
                else:
                    data_entrega = datetime.now
            
            # Verifica em serviço
            if em_servico:
                cliente.em_servico = True
            else: 
                cliente.em_servico = False
            
            # Salvando as alterações
            cliente.nome = nome
            cliente.chassi = chassi
            cliente.telefone = telefone
            cliente.cpf = cpf
            cliente.placa = placa
            cliente.data_encerramento = data_entrega
            cliente.servico = servico
            cliente.valor_servico = valor_servico
            cliente.valor_pecas = valor_pecas
            cliente.save()
            
            return redirect('lista_de_clientes', nome_da_oficina=nome_da_oficina, chave=chave)
        
        return render(request, 'editar_cliente.html', {'nome_da_oficina': nome_da_oficina, 'cliente_id':cliente_id, 'chave': chave})


















