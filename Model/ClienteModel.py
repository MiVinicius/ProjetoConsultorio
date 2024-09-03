import sys
sys.path.append('.')
from ProjetoConsultorio.Model.PessoaModelAbstract import Pessoa
class Cliente(Pessoa):
    
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome, cpf, telefone, endereco)
        self.__consulta = []
        
    @property
    def consulta(self):
        return self.__consulta
    
    @consulta.setter
    def consulta(self, consulta):
        self.__consulta.append(consulta)
        
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self._nome == other._nome and self._cpf == other._cpf
        return False
        
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}"
    
    def mostrarConsultas(self):
        for consulta in self.__consulta:
            print(f'Descrição: {consulta.descricao} - Data: {consulta.data} - Numero da consulta: {consulta.numero} - Cliente: {consulta.cliente}', end='\n\n')
    
    def mostrarInformacoes(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}')
