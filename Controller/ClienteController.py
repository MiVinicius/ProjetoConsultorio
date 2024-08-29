import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

class ClienteController():
    
    @staticmethod
    def cadastrarCliente():
        nome = str(input("Digite o nome do novo Cliente: \n"))
        cpf = str(input("Digite o CPF do novo cliente: \n"))
        if BancoDadosController.buscarCliente(nome, cpf) is None:
            endereco = EnderecoController.cadastrarEndereco()
            BancoDadosController.cadastrarCliente(nome, cpf, endereco)
            print("cadastro do cliente sucedido!")
            input("pressione ENTER para continuar")
            return True
        else: 
            print("o cliente já existe!")
            input("pressione ENTER para continuar")
            return False
    
    @staticmethod
    def buscarCliente():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF para procurar: \n"))
        if BancoDadosController.buscarCliente(nome, cpf) is None:
            print("o cliente não existe!")
            input("pressione ENTER para continuar")
        else:
            print(BancoDadosController.buscarCliente(nome, cpf).__str__())
            input("pressione ENTER para continuar")
        
    
    @staticmethod
    def buscarCliente2():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF para procurar: \n"))
        if BancoDadosController.buscarCliente(nome, cpf) is None:
            return None
        else:
            return BancoDadosController.buscarCliente(nome, cpf)
        
    
    @staticmethod
    def modificarCliente():
        nomeModificar = str(input("Digite o nome do cliente para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        if BancoDadosController.buscarCliente(nomeModificar, cpfModificar) is None:
            print("o cliente não existe!")
            input("pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do cliente: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            if BancoDadosController.modificarCliente(BancoDadosController.buscarCliente(nomeModificar, cpfModificar), nomeNovo, cpfNovo):
                return f'o cliente {nomeNovo} foi Atualizado'
            else:
                return f'o cliente {nomeNovo} não foi Atualizado'
    
    @staticmethod
    def deletarCliente():
        return BancoDadosController.deletarCliente(ClienteController.buscarCliente2())
            
            
        
        