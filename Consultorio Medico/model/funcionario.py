from .pessoa import Pessoa
from abc import ABC, abstractmethod

class Funcionario(Pessoa, ABC):
    def __init__(self, nome, cpf, endereco, login, senha, salario):
        super().__init__(nome, cpf, endereco)
        self.__login = login
        self.__senha = senha
        self.__salario = salario

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha

    @property
    def salario(self):
        return self.__salario

    @login.setter
    def login(self, login):
        self.__login = login

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def autenticar(self, login, senha):
        return self.__login == login and self.__senha == senha

    @abstractmethod
    def exibir_detalhes(self):
        pass
