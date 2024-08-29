import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

class MedicoController():
    @staticmethod
    def cadastrarMedico():
        nome = str(input("Digite o nome do Médico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarMedico(nome, cpf) is None:
            endereco = EnderecoController.cadastrarEndereco()
            BancoDadosController.cadastrarMedico(nome, cpf, endereco)
            print("cadastro do médico sucedido!")
            input("pressione ENTER para continuar")
            return True
        else: 
            print("o medico já existe!")
            input("pressione ENTER para continuar")
            return False
    
    @staticmethod
    def buscarMedico():
        nome = str(input("Digite o nome do medico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarMedico(nome, cpf) is None:
            print("o medico não existe!")
            input("pressione ENTER para continuar")
        else: 
            print(BancoDadosController.buscarMedico(nome, cpf).__str__())
            input("pressione ENTER para continuar")
            
    @staticmethod
    def buscarMedico2():
        nome = str(input("Digite o nome do medico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarMedico(nome, cpf) is None:
            return None
        else:
            return BancoDadosController.buscarMedico(nome, cpf)
        
    
    @staticmethod
    def modificarMedico():
        nomeModificar = str(input("Digite o nome do cliente para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        if BancoDadosController.buscarMedico(nomeModificar, cpfModificar) is None:
            print("o medico não existe!")
            input("pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do cliente: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            if BancoDadosController.modificarMedico(BancoDadosController.buscarMedico(nomeModificar, cpfModificar), nomeNovo, cpfNovo):
                return f'o medico {nomeNovo} foi Atualizado'
            else:
                return f'o medico {nomeNovo} não foi Atualizado'
        
    
    @staticmethod
    def deletarMedico():
        return BancoDadosController.deletarMedico(MedicoController.buscarMedico2())