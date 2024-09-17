import re
import sys
sys.path.append('.')
from ProjetoConsultorio.Model.FuncionarioModelAbstract import Funcionario

class Medico(Funcionario):
    
    def __init__(self, nome, cpf, DataNasc, telefone, endereco, salario, crm):
        super().__init__(nome, cpf, DataNasc, telefone, endereco, salario)
        self._crm = crm

    @property
    def crm(self) -> str:
        return self._crm
    
    @crm.setter
    def crm(self, crm: str) -> str:
        self._crm = crm
        
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Cpf: {self.cpf}, Data de Nascimento: {self.DataNasc}, Telefone: {self.telefone}, "
            f"Endereço: {self.endereco_id}, Salário: {self.salario}, CRM: {self.crm}")
        
    @staticmethod
    def validar_cpf(cpf: str) -> str:
        cpf_limpo = re.sub(r'[\s.-]', '', cpf)
        if not cpf_limpo.isdigit():
            raise ValueError("CPF deve conter apenas números.")
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        return cpf_limpo

    def __eq__(self, other):
        if isinstance(other, Medico):
            return (self.nome == other.nome and self.cpf == other.cpf and 
                    self.telefone == other.telefone and self.endereco_id == other.endereco_id and 
                    self.salario == other.salario and self.crm == other.crm)
        return False

    def __repr__(self):
        return (f"Nome: {self.nome}, Cpf: {self.cpf}, Data de Nascimento: {self.DataNasc}, Telefone: {self.telefone}, "
                f"Endereço: {self.endereco_id}, Salário: {self.salario}, CRM: {self.crm}")
