import sys
sys.path.append('.')
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario

class Medico(Funcionario):
    
    def __init__(self, nome, cpf, Endereco = None):
        super().__init__(nome, cpf, Endereco)
        self.__salario = 3212   
    
    def _getNome(self):
        return super()._getNome()
    
    def _setNome(self, nome):
        super()._setNome(nome)
        
    def _getCpf(self):
        return super()._getCpf()
    
    def _setCpf(self, cpf):
        super()._setCpf(cpf)
    
    def _getSalario(self):
        return self.__salario
    
    def _setSalario(self, salario):
        self.__salario - salario
        
    def _getEndereco(self):
        return self._endereco
    
    def _setEndereco(self, endereco):
        self._endereco = endereco
        
    def __eq__(self, other):
        if isinstance(other, Medico):
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self):
        return f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Salário: {self.__salario}"