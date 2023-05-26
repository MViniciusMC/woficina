from django.db import models

# Create your models here

class Login(models.Model):
    usuario =  models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=8, null=False, blank=False)
    def __str__ (self): 
        return f"Cliente [usuario={self.usuario},senha={self.senha}]"
class Cliente(models.Model):
    nome =  models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=100, null=False, blank=False)
    chassi = models.CharField(max_length=100, default='0') 
    telefone = models.CharField(max_length=14,default='0')
    placa = models.CharField(max_length=14,default='0')
    em_servico = models.BooleanField(default=False)
    def __str__(self):
        return f"Cliente [nome = {self.nome}]"
    
