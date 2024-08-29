import sys
sys.path.append('.')
class Cliente():
    
    def __init__(self, nome, cpf, Endereco = None):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = Endereco
        self.__consulta = []
        
    def _getNome(self):
        return self.__nome
    
    def _setNome(self, nome):
        self.__nome = nome
        
    def _getCpf(self):
        return self.__cpf
    
    def _setCpf(self, cpf):
        self.__cpf = cpf
    
    def _getEndereco(self):
        return self.__endereco
    
    def _setEndereco(self, Endereco):
        self.__endereco = Endereco
        
    def _getConsulta(self):
        for consulta in self.__consulta:
            print(f'Descrição: {consulta.descricao} - Data: {consulta.data} - Numero da consulta: {consulta.numero} - Cliente: {consulta.cliente}')
    
    def _setConsulta(self, consulta):
        self.__consulta.append(consulta)
        
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self) -> str:
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Endereço: {self.__endereco}"
    