import sys
sys.path.append('.')
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario

class Medico(Funcionario):
    
    def __init__(self, nome, cpf, telefone, Endereco, salario, crm):
        super().__init__(nome, cpf, telefone, Endereco, salario)
        self._crm = crm
    
    def _getNome(self):
        return super()._getNome()
    
    def _setNome(self, nome):
        super()._setNome(nome)
        
    def _getCpf(self):
        return super()._getCpf()
    
    def _setCpf(self, cpf):
        super()._setCpf(cpf)
        
    def _getTelefone(self):
        return super()._getTelefone()
    
    def _setTelefone(self, telefone):
        super()._setTelefone(telefone)
    
    def _getSalario(self):
        return super()._getSalario()
    
    def _setSalario(self, salario):
        super()._setSalario(salario)
        
    def _getEndereco(self):
        return super()._getEndereco()
    
    def _setEndereco(self, endereco):
        super()._setEndereco(endereco)
        
    def _getCrm(self):
        return self._crm
    
    def _setCrm(self, crm):
        self._crm = crm
        
    def __eq__(self, other):
        if isinstance(other, Medico):
            return self._nome == other._nome and self._cpf == other._cpf
        return False
        
    def __repr__(self):
        return f"Nome: {self._nome}, Cpf: {self._cpf}, Endereço: {self._endereco}, Salário: {self._salario}"