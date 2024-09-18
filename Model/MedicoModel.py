import re
import sys
sys.path.append('.')
from Model.FuncionarioModelAbstract import Funcionario
from typing import Optional

class Medico(Funcionario):
    
    def __init__(self, nome: str, cpf: str, DataNasc: str, telefone: str, endereco_id: Optional[int], salario: float, crm: str):
        super().__init__(nome, cpf, DataNasc, telefone, endereco_id, salario)
        self._crm = self._validar_crm(crm)

    def _validar_crm(self, crm: str) -> str:
        if not crm:
            raise ValueError("CRM não pode ser vazio.")
        crm_formatado = crm.strip()
        if not re.match(r'^[A-Za-z0-9]+$', crm_formatado):
            raise ValueError("CRM deve conter apenas letras e números.")
        if len(crm_formatado) < 5 or len(crm_formatado) > 20:
            raise ValueError("CRM deve ter entre 5 e 20 caracteres.")
        return crm_formatado
    
    @property
    def crm(self) -> str:
        return self._crm
    
    @crm.setter
    def crm(self, crm: str):
        self._crm = self._validar_crm(crm)
        
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
