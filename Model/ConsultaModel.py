import sys
sys.path.append('.')


class Consulta:
    
    __contador = 0 
    
    def __init__(self, descricao, data, horario, valor, cliente):
        self.__descricao = descricao
        self.__data = data
        self.__horario = horario
        self.__cliente = cliente
        self.__valor = valor
        Consulta.__contador += 1  # Incrementa o contador de classe
        self.__numero = Consulta.__contador

        
    def _getDescricao(self):
        return self.__descricao
    
    def _setDescricao(self, descricao):
        self.__descricao = descricao
        
    def _getData(self):
        return self.__data
    
    def _setData(self, data):
        self.__data = data
        
    def _getHorario(self):
        return self.__horario
    
    def _setHorario(self, horario):
        self.__horario = horario

    def _getCliente(self):
        return self.__cliente
    
    def _setCliente(self, cliente):
        self.__cliente = cliente
        
    def _getNumero(self):
        return self.__numero
    
    def _getValor(self):
        return self.__valor
    
    def _setValor(self, valor):
        self.__valor = valor
    
    def __str__(self):
        return f"Número da consulta: {self.__numero}\nDescrição: {self.__descricao}\nData: {self.__data}\nHorário: {self.__horario}\nValor: {self.__valor}\nCliente CPF: {self.__cliente}"
    
    def __repr__(self):
        return f"Número da consulta: {self.__numero}\nDescrição: {self.__descricao}\nData: {self.__data}\nHorário: {self.__horario}\nValor: {self.__valor}\nCliente CPF: {self.__cliente}"