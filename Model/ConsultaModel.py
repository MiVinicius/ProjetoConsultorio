import sys
sys.path.append('.')
import re
from datetime import datetime

class _InvalidDataError(Exception):
    """Classe interna para erros de dados inválidos."""
    pass

class Consulta:
    def __init__(self, descricao, data, horario, valor, cliente, medico, numero=None):
        self.__descricao = self.__validar_descricao(descricao)  # agora sim os dados são validados
        self.__data = self.__validar_data(data)
        self.__horario = self.__validar_horario(horario)
        self.__valor = self.__validar_valor(valor)
        self.__cliente = self.__validar_cliente(cliente)
        self.__medico = self.__validar_medico(medico)
        self.__numero = numero

    @property
    def descricao(self):
        return self.__descricao

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def valor(self):
        return self.__valor

    @property
    def cliente(self):
        return self.__cliente

    @property
    def numero(self):
        return self.__numero

    @property
    def medico(self):
        return self.__medico

    def __validar_descricao(self, descricao):
        if not descricao or not isinstance(descricao, str):
            raise _InvalidDataError("Descrição não pode ser vazia.")
        return descricao

    def __validar_data(self, data):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return data
        except ValueError:
            raise _InvalidDataError("A data deve estar no formato dd/mm/yyyy.")

    def __validar_horario(self, horario):
        if not re.match(r'^[0-2][0-9]:[0-5][0-9]$', horario):
            raise _InvalidDataError("O horário deve estar no formato hh:mm.")
        return horario

    def __validar_valor(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise _InvalidDataError("O valor deve ser um número não negativo.")
        return valor

    def __validar_cliente(self, nome):
        if not nome or not isinstance(nome, str):
            raise _InvalidDataError("CPF de cliente não pode ser vazio.")
        return nome
    
    def __validar_medico(self, nome):
        if not nome or not isinstance(nome, str):
            raise _InvalidDataError("CRM de médico não pode ser vazio.")
        return nome

    def __eq__(self, other):  # Resquício de uma era perdida... 
        if isinstance(other, Consulta):
            return self.numero == other.numero
        return False

    def __repr__(self):
        return (f"Número da consulta: {self.numero}\nDescrição: {self.descricao}\n"
                f"Data: {self.data}\nHorário: {self.horario}\nValor: {self.valor}\n"
                f"Cliente CPF: {self.cliente}\nMédico CRM: {self.medico}")
        

