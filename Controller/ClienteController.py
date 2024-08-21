from Model.ClienteModel import Cliente
from Controller.BancoDadosController import BancoDadosController

class ClienteController():
    @staticmethod
    def cadastrarCliente():
        cliente = Cliente(str(input("Digite o nome do Cliente: \n")), str(input("Digite o CPF: \n")))
        if BancoDadosController.buscarCliente(cliente) is None:
            BancoDadosController.cadastrarCliente(cliente)
            print("cadastro do cliente sucedido!")
            return True
        else: 
            print("o cliente já existe!")
            return False
    
    @staticmethod
    def buscarCliente():
        cliente = Cliente(str(input("Digite o nome do cliente: \n")), str(input("Digite o CPF: \n")))
        return BancoDadosController.buscarCliente(cliente)
    
    @staticmethod
    def modificarCliente():
        cliente = Cliente(str(input("Digite o nome do cliente: \n")), str(input("Digite o CPF: \n")))
        cliente_novo = Cliente(str(input("Digite o novo nome do cliente: \n")), str(input("Digite o novo CPF: \n")))
        return BancoDadosController.modificarCliente(BancoDadosController.buscarCliente(cliente), cliente_novo)
    
    @staticmethod
    def deletarCliente():
        return BancoDadosController.deletarCliente(ClienteController.buscarCliente())
            
            
        
        