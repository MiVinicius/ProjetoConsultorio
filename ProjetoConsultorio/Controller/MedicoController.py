from Model.MedicoModel import Medico 
from Controller.BancoDadosController import BancoDadosController

class MedicoController():
    @staticmethod
    def cadastrarMedico():
        medico = Medico(str(input("Digite o nome do Médico: \n")), str(input("Digite o CPF: \n")))
        if BancoDadosController.buscarMedico(medico) is None:
            BancoDadosController.cadastrarMedico(medico)
            print("cadastro do médico sucedido!")
            return True
        else: 
            print("o medico já existe!")
            return False
    
    @staticmethod
    def buscarMedico():
        medico = Medico(str(input("Digite o nome do medico: \n")), str(input("Digite o CPF: \n")))
        return BancoDadosController.buscarMedico(medico)
    
    @staticmethod
    def modificarMedico():
        medico = Medico(str(input("Digite o nome do Médico: \n")), str(input("Digite o CPF: \n")))
        medico_novo = Medico(str(input("Digite o novo nome do Médico: \n")), str(input("Digite o novo CPF: \n")))
        return BancoDadosController.modificarMedico(BancoDadosController.buscarMedico(medico), medico_novo)
    
    @staticmethod
    def deletarMedico():
        return BancoDadosController.deletarMedico(MedicoController.buscarMedico())