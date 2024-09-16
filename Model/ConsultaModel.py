import sys
sys.path.append('.')


class Consulta:
    
    
    def __init__(self, descricao, data, horario, valor, cliente, medico, numero=None):
        self.__descricao = descricao
        self.__data = data
        self.__horario = horario
        self.__valor = valor
        self.__cliente = cliente
        self.__numero = numero
        self.__medico = medico

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    def __eq__(self, other):
        if isinstance(other, Consulta):
            return self.numero == other.numero
        return False

    def __repr__(self):
        return (f"Número da consulta: {self.numero}\nDescrição: {self.descricao}\n"
                f"Data: {self.data}\nHorário: {self.horario}\nValor: {self.valor}\n"
                f"Cliente CPF: {self.cliente}\nMédico CRM: {self.medico}")
