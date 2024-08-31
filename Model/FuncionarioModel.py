import sys
from ProjetoConsultorio.Model.PessoaModelAbstract import Pessoa
sys.path.append('.')
class Funcionario(Pessoa):
    
    def __init__(self, nome, cpf, telefone, Endereco, salario):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._endereco = Endereco
        self._salario = salario
        
    def _getNome(self):
        return self._nome
    
    def _setNome(self, nome):
        self._nome = nome
        
    def _getCpf(self):
        return self._cpf
    
    def _setCpf(self, cpf):
        self._cpf = cpf
        
    def _getTelefone(self):
        return self._telefone
    
    def _setTelefone(self, telefone):
        self._telefone = telefone
        
    def _getSalario(self):
        return self._salario
    
    def _setSalario(self, salario):
        self._salario = salario
        
    def _getEndereco(self):
        return self._endereco
    
    def _setEndereco(self, endereco):
        self._endereco = endereco
        
    def __eq__(self, other):
        if isinstance(other, Funcionario):
            return self._nome == other._nome and self._cpf == other._cpf
        return False
        
    def __repr__(self):
        return f"Nome: {self._nome}, Cpf: {self._cpf}, Telefone: {self._telefone}, Endereço: {self._endereco}, Salário: {self._salario}"