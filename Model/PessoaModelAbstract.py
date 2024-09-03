import sys
sys.path.append('.')
from abc import ABC, abstractmethod

class Pessoa(ABC):
    
    def __init__(self, nome, cpf, telefone, endereco):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._endereco = endereco
        
    @property
    def nome(self):
        return self._nome  # Corrigido: Adicionado return
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome  # Corrigido: Removido return e atribuição correta

    @property
    def cpf(self):
        return self._cpf  # Corrigido: Adicionado return
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf  # Corrigido: Removido return e atribuição correta

    @property
    def telefone(self):
        return self._telefone  # Corrigido: Adicionado return
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone  # Corrigido: Removido return e atribuição correta

    @property
    def endereco(self):
        return self._endereco  # Corrigido: Adicionado return
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco  # Corrigido: Removido return e atribuição correta
    
    @abstractmethod
    def mostrarInformacoes(self):
        pass