import sys
sys.path.append('.')


class Consulta:
    
    __nConsulta = 0 
    
    def __init__(self, descricao, data, cliente= None):
        self.descricao = descricao
        self.data = data
        self.numero = self.incrementar_consulta()
        self.cliente = cliente
        
    @classmethod
    def incrementar_consulta(cls): 
        cls.__nConsulta += 1
        return cls.__nConsulta
        
    def _getDescricao(self):
        return self.descricao
    def _setDescricao(self, descricao):
        self.descricao = descricao
    def _getData(self):
        return self.data
    def _setDescricao(self, data):
        self.data = data       
    
    def setCliente(self, cliente):
        self.cliente = cliente
    def getNumero(self):
        return self.numero
    def __str__(self):
        return f"Número da consulta: {self.numero}\nDescrição: {self.descricao}\nData: {self.data}"