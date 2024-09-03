import sys
sys.path.append('.')
from abc import ABC, abstractmethod
from ProjetoConsultorio.Model.PessoaModelAbstract import Pessoa

class Funcionario(Pessoa, ABC ):
    
    def __init__(self, nome, cpf, telefone, salario, endereco):
        super().__init__(nome, cpf, telefone, endereco)
        self.__salario = float(salario)

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario
        
    @abstractmethod
    def mostrarInformacoes(self):
        return super().mostrarInformacoes()
        
