import re
import sys
sys.path.append('.')
from ProjetoConsultorio.Model.FuncionarioModelAbstract import Funcionario
from typing import Optional

class Atendente(Funcionario):
    
    def __init__(self,nome: str, cpf: str, DataNasc: str, telefone: str, endereco_id: Optional[int], salario: float):
        super().__init__(nome, cpf, DataNasc, telefone, endereco_id, salario)
        
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Cpf: {self.cpf}, Data de Nascimento: {self.DataNasc}, Telefone: {self.telefone}, "
            f"Endereço: {self.endereco_id}, Salário: {self.salario}")
    
    @staticmethod
    def validar_cpf(cpf: str) -> str:
        cpf_limpo = re.sub(r'[\s.-]', '', cpf)
        if not cpf_limpo.isdigit():
            raise ValueError("CPF deve conter apenas números.")
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        return cpf_limpo
    
    def __eq__(self, other):
        if isinstance(other, Atendente):
            return self.nome == other.nome and self.cpf == other.cpf
        return False
        
    def __repr__(self):
        return (f"Nome: {self.nome}, Cpf: {self.cpf}, Data de Nascimento: {self.DataNasc}, Telefone: {self.telefone}, "
            f"Endereço: {self.endereco_id}, Salário: {self.salario}")