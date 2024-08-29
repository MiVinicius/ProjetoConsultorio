import sys
sys.path.append('.')
import random

class Consulta:
    
    _contador = 0 
    
    def __init__(self, descricao, data, cliente):
        self.descricao = descricao
        self.data = data
        self.cliente = cliente
        self.valor = random.randint(100, 500)  # Cria um valor aleatório entre 100 e 500
        Consulta._contador += 1  # Incrementa o contador de classe
        self.numero = Consulta._contador

        
    def _getDescricao(self):
        return self.descricao
    
    def _setDescricao(self, descricao):
        self.descricao = descricao
        
    def _getData(self):
        return self.data
    
    def _setData(self, data):
        self.data = data

    def _getCliente(self):
        return self.cliente
    
    def _setCliente(self, cliente):
        self.cliente = cliente
        
    def getNumero(self):
        return self.numero
    
    def getValor(self):
        return self.valor
    
    def __str__(self):
        return f"Número da consulta: {self.numero}\nDescrição: {self.descricao}\nData: {self.data}\nCliente: {self.cliente}"