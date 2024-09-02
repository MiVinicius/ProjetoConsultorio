from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def endereco(self):
        return self.__endereco

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @abstractmethod
    def exibir_detalhes(self):
        pass
