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
        
    def _getNome(self):
        return self.__nome
    
    def _setNome(self, nome):
        self.__nome = nome
        
    def _getCpf(self):
        return self.__cpf
    
    def _setCpf(self, cpf):
        self.__cpf = cpf
        
    def _getTelefone(self):
        return self.__telefone
    
    def _setTelefone(self, telefone):
        self.__telefone = telefone
    
    def _getEndereco(self):
        return self.__endereco
    
    def _setEndereco(self, Endereco):
        self.__endereco = Endereco
        
    def _getConsulta(self):
        return self.__consulta
    
    def _setConsulta(self, consulta):
        self.__consulta.append(consulta)
        
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self) -> str:
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Telefone: {self.__telefone}, Endereço: {self.__endereco}"
    
    def mostrarConsultas(self):
        for consulta in self.__consulta:
            print(f'Descrição: {consulta.__descricao} - Data: {consulta.__data} - Numero da consulta: {consulta.__numero} - Cliente: {consulta.__cliente}')
    