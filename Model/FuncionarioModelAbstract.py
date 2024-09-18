import sys
sys.path.append('.')
from abc import ABC, abstractmethod
from Model.PessoaModelAbstract import Pessoa
from typing import Optional

class Funcionario(Pessoa, ABC):
    _salario: float

    def __init__(self, nome: str, cpf: str, DataNasc: str, telefone: str, endereco_id: Optional[int], salario: float):
        super().__init__(nome, cpf, DataNasc, telefone, endereco_id)  
        self._salario = self._validar_salario(salario)
        
    def _validar_salario(self, salario: float) -> float:
        if salario < 0:
            raise ValueError("O salário não pode ser negativo!")
        return salario

    @property
    def salario(self) -> float:
        return self._salario

    @abstractmethod
    def mostrar_informacoes(self):
        pass
        
