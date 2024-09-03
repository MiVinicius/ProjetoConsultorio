from abc import ABC, abstractmethod

class Pessoa(ABC):
    
    def __init__(self):
        pass
        
    @property
    @abstractmethod
    def nome(self):
        pass
    
    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    @abstractmethod
    def cpf(self):
        pass
    
    @cpf.setter
    @abstractmethod
    def cpf(self, cpf):
        pass

    @property
    @abstractmethod
    def telefone(self):
        pass
    
    @telefone.setter
    @abstractmethod
    def telefone(self, telefone):
        pass

    @property
    @abstractmethod
    def endereco(self):
        pass
    
    @endereco.setter
    @abstractmethod
    def endereco(self, endereco):
        pass