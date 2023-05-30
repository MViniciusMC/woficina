from django.db import models
from datetime import datetime
# Create your models here
import random 
class CadastroOficina(models.Model):
    oficina = models.CharField(max_length=100, null=False, blank=False)
    chave = models.CharField( max_length=150,null=False, blank=False)
    def __str__ (self): 
        return f"Cliente [oficina={self.oficina},chave={self.chave}]"
class Cliente(models.Model):
    nome =  models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=100, null=False, blank=False)
    chassi = models.CharField(max_length=100, default='0') 
    telefone = models.CharField(max_length=14,default='0')
    placa = models.CharField(max_length=14,default='0')
    em_servico = models.BooleanField(default=False)
    servico = models.CharField(max_length=300, default='')
    oficina = models.CharField(max_length=25, default='')
    valor_pecas = models.FloatField( default=0)
    valor_servico = models.FloatField( default=0)
    data_encerramento = models.DateTimeField(default=datetime.now, blank=False)
    data_incio =  models.DateTimeField(default=datetime.now, blank=False)
    def __str__(self):
        return f"Cliente [nome = {self.nome}]"


    
