from model_pessoa import ModelPessoa
from abc import ABC, abstractmethod

class ModelFuncionario(ModelPessoa, ABC):
    def __init__(self, nome, cpf, endereco, telefone, login, senha, salario, cargo):
        super().__init__(nome, cpf, endereco, telefone)
        self.__login = login
        self.__senha = senha
        self._salario = salario
        self._cargo = cargo

    @property
    def login(self):
        return self.__login

    def verificar_senha(self, senha):
        return self.__senha == senha

    @abstractmethod
    def mostrar_informacoes(self):
        pass
