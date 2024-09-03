import sys
from ProjetoConsultorio.Model.FuncionarioModelAbstract import Funcionario
sys.path.append('.')
class Atendente(Funcionario):
    
    def __init__(self, nome, cpf, telefone, endereco, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

        
    def __eq__(self, other):
        if isinstance(other, Atendente):
            return self.nome == other.nome and self.cpf == other.cpf
        return False
        
    def __repr__(self):
        return (f"Nome: {self.nome}, Cpf: {self.cpf}, Telefone: {self.telefone}, "
            f"Endereço: {self.endereco}, Salário: {self.salario}")