from abc import ABC, abstractmethod

class ModelPessoa(ABC):
    def __init__(self, nome, cpf, endereco, telefone):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        return self._telefone

    @abstractmethod
    def mostrar_informacoes(self):
        pass
