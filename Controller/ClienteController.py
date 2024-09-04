import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

class ClienteController:
    
    def __init__(self, banco_dados_controller):
        self.banco_dados_controller = banco_dados_controller
    
    def cadastrarCliente(self):
        try:
            nome = input("Digite o nome do novo Cliente: \n")
            cpf = input("Digite o CPF do novo cliente: \n")
            cliente_existe = self.banco_dados_controller.buscarCliente(nome, cpf)
            if cliente_existe is None:
                telefone = input("Digite o telefone do novo cliente: \n")
                endereco = EnderecoController.cadastrarEndereco() # eu sei que tem como fazer isso melhor
                self.banco_dados_controller.cadastrarCliente(nome, cpf, telefone, endereco)
                print("Cadastro do cliente realizado com sucesso!")
                input("Pressione ENTER para continuar")
                return True
            else: 
                print("O cliente já existe!")
                input("Pressione ENTER para continuar")
                return False
        except Exception as e:
            print("Ocorreu um erro ao cadastrar o cliente:", e)
            input("Pressione ENTER para continuar")
            return False
        
    def buscarCliente(self):
        nome = input("Digite o nome do cliente para procurar: \n")
        cpf = input("Digite o CPF para procurar: \n")
        cliente_existe = self.banco_dados_controller.buscarCliente(nome, cpf)
        if cliente_existe is None:
            print("O cliente não existe!")
            input("Pressione ENTER para continuar")
        else:
            print(cliente_existe)
            input("Pressione ENTER para continuar")
        
    def buscarCliente2(self):
        nome = input("Digite o nome do cliente para procurar: \n")
        cpf = input("Digite o CPF para procurar: \n")
        return self.banco_dados_controller.buscarCliente(nome, cpf)
        
    def modificarCliente(self):
        nomeModificar = input("Digite o nome do cliente para buscar: \n")
        cpfModificar = input("Digite o CPF para buscar: \n")
        cliente_existe = self.banco_dados_controller.buscarCliente(nomeModificar, cpfModificar)
        if cliente_existe is None:
            print("O cliente não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            nomeNovo = input("Digite o novo nome do cliente: \n")
            cpfNovo = input("Digite o novo CPF: \n")
            telefone = input("Digite o novo telefone do cliente: \n")
            endereco = EnderecoController.cadastrarEndereco()
            cliente_novo = self.banco_dados_controller.modificarCliente(cliente_existe, nomeNovo, cpfNovo, telefone, endereco)
            if cliente_novo:
                print(f"O cliente {nomeNovo} foi atualizado com sucesso!")
                input("Pressione ENTER para continuar")
                return True
            else:
                print("Ocorreu um erro ao atualizar o cliente")
                input("Pressione ENTER para continuar")
                return False
    
    def deletarCliente(self):
        try:
            clienteDeletar = self.buscarCliente2()
            if clienteDeletar is None:
                print("O cliente não existe!")
                input("Pressione ENTER para continuar")
                return False
            if clienteDeletar.consulta:
                for consulta in clienteDeletar.consulta:
                    self.banco_dados_controller.deletarConsulta(consulta)
            self.banco_dados_controller.deletarCliente(clienteDeletar)
            print("Cliente deletado com sucesso!")
            input("Pressione ENTER para continuar")
            return True
        except Exception as e:
            print("Ocorreu um erro ao deletar o cliente:", e)
            input("Pressione ENTER para continuar")
            return False


            
            
        
        