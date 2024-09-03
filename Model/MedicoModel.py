import sys
sys.path.append('.')
from ProjetoConsultorio.Model.FuncionarioModelAbstract import Funcionario

class Medico(Funcionario):
    
    def __init__(self, nome, cpf, telefone, endereco, salario, crm):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._endereco = endereco
        self._salario = salario
        self._crm = crm

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def crm(self):
        return self._crm
    
    @crm.setter
    def crm(self, crm):
        self._crm = crm
        
    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}, Cpf: {self.cpf}, Telefone: {self.telefone}, "
            f"Endereço: {self.endereco}, Salário: {self.salario}, CRM: {self.crm}")

    def __eq__(self, other):
        if isinstance(other, Medico):
            return (self.nome == other.nome and self.cpf == other.cpf and 
                    self.telefone == other.telefone and self.endereco == other.endereco and 
                    self.salario == other.salario and self.crm == other.crm)
        return False

    def __repr__(self):
        return (f"Nome: {self.nome}, Cpf: {self.cpf}, Telefone: {self.telefone}, "
                f"Endereço: {self.endereco}, Salário: {self.salario}, CRM: {self.crm}")
