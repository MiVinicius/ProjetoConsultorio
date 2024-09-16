import sys
sys.path.append('.')
from abc import ABC, abstractmethod
from ProjetoConsultorio.Model.PessoaModelAbstract import Pessoa

class Funcionario(Pessoa, ABC ):
    
    def __init__(self, nome, cpf, DataNasc, telefone, endereco, salario):
        super().__init__(nome, cpf, DataNasc, telefone, endereco)
        self._salario = float(salario)

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        salario_str = str(salario).replace('.', '').replace(',', '.')
        salario_float = float(salario_str)
        if salario_float < 0:
            raise ValueError("O salário não pode ser negativo!")
        
    @abstractmethod
    def mostrar_informacoes(self):
        pass
        
