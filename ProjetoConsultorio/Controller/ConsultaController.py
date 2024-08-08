from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController

class consultaController():
    
    def cadastrarConsulta(cliente):
        descricao = str(input("Digite a descrição da consulta: \n"))
        data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
        consulta = Consulta(descricao, data)
        (Cliente(cliente))._setConsulta(consulta)
        BancoDadosController.cadastrarConsulta(consulta)
        print(f"Consulta adicionada para o cliente {cliente._nome}")
        
    def buscarConsulta():
        descricao = str(input("Digite a descrição da consulta: \n"))
        data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
        consulta = Consulta(descricao, data)
        return BancoDadosController.buscarConsulta(consulta)
    
    def modificarConsulta():
        consulta = consultaController.buscarConsulta()
        if consulta != None:
            descricao = str(input("Digite a descrição da consulta: \n")) 
            data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
            consulta_nova = Consulta(descricao, data)
            return BancoDadosController.modificarConsulta(consulta, consulta_nova)
            
    def deletarConsulta():
        pass