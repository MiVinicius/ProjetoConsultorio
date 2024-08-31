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