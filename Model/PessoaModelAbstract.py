from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def _getNome(self):
        pass

    @abstractmethod
    def _getCpf(self):
        pass

    @abstractmethod
    def _getTelefone(self):
        pass

    @abstractmethod
    def _getEndereco(self):
        pass
    
    @abstractmethod
    def _setNome(self, nome):
        pass

    @abstractmethod
    def _setCpf(self, cpf):
        pass
    
    @abstractmethod
    def _setTelefone(self, telefone):
        pass

    @abstractmethod
    def _setEndereco(self, endereco):
        pass