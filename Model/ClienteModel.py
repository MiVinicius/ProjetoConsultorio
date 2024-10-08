import re
import sys
sys.path.append('.')
from Model.PessoaModelAbstract import Pessoa
from typing import Optional

class Cliente(Pessoa):
    
    def __init__(self, nome: str, cpf: str, DataNasc: str, telefone: str, endereco_id: Optional[int]):
        super().__init__(nome, cpf, DataNasc, telefone, endereco_id)
        
    @staticmethod
    def validar_cpf(cpf: str) -> str:
        cpf_limpo = re.sub(r'[\s.-]', '', cpf)
        if not cpf_limpo.isdigit():
            raise ValueError("CPF deve conter apenas números.")
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        return cpf_limpo
        
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self._nome == other._nome and self._cpf == other._cpf
        return False
        
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.DataNasc}, Telefone: {self.telefone}, Endereço: {self.endereco_id}"
    
    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.DataNasc}, Telefone: {self.telefone}, Endereço: {self.endereco_id}')
        
