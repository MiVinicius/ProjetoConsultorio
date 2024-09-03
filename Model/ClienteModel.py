import sys
sys.path.append('.')
from ProjetoConsultorio.Model.EnderecoModel import Endereco
from ProjetoConsultorio.Model.PessoaModelAbstract import Pessoa
class Cliente(Pessoa):
    
    def __init__(self, nome, cpf, telefone, endereco:Endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__consulta = []
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
        
    @property
    def consulta(self):
        return self.__consulta
    
    @consulta.setter
    def consulta(self, consulta):
        self.__consulta.append(consulta)
        
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}"
    
    def mostrarConsultas(self):
        for consulta in self.__consulta:
            print(f'Descrição: {consulta.descricao} - Data: {consulta.data} - Numero da consulta: {consulta.numero} - Cliente: {consulta.cliente}', end='\n\n')
    