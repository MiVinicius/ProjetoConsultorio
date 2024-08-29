import sys
sys.path.append('.')
class Funcionario():
    
    def __init__(self, nome, cpf, Endereco = None):
        self._nome = nome
        self._cpf = cpf
        self._endereco = Endereco
        self._salario = 1412
        
    def _getNome(self):
        return self._nome
    
    def _setNome(self, nome):
        self._nome = nome
        
    def _getCpf(self):
        return self._cpf
    
    def _setCpf(self, cpf):
        self._cpf = cpf
        
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
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self):
        return f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Salário: {self.__salario}"