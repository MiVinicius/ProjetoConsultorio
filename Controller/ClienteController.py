import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

class ClienteController():
    
    
    def cadastrarCliente():
        try:
            nome = str(input("Digite o nome do novo Cliente: \n"))
            cpf = str(input("Digite o CPF do novo cliente: \n"))
            cliente_existe = BancoDadosController.buscarCliente(nome, cpf)
            if cliente_existe is None:
                telefone = str(input("Digite o telefone do novo cliente: \n"))
                endereco = EnderecoController.cadastrarEndereco()
                BancoDadosController.cadastrarCliente(nome, cpf, telefone, endereco)
                print("cadastro do cliente sucedido!")
                input("pressione ENTER para continuar")
                return True
            else: 
                print("o cliente já existe!")
                input("pressione ENTER para continuar")
                return False
        except Exception as e:
                print("ocorreu um erro ao cadastrar o cliente: ", e)
                input("pressione ENTER para continuar")
                return False
        
    
    def buscarCliente():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF para procurar: \n"))
        cliente_existe = BancoDadosController.buscarCliente(nome, cpf)
        if cliente_existe is None:
            print("o cliente não existe!")
            input("pressione ENTER para continuar")
        else:
            print(cliente_existe.__str__())
            input("pressione ENTER para continuar")
        
    
    def buscarCliente2():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF para procurar: \n"))
        cliente_existe = BancoDadosController.buscarCliente(nome, cpf)
        if cliente_existe is None:
            return None
        else:
            return cliente_existe
        
    
    def modificarCliente():
        nomeModificar = str(input("Digite o nome do cliente para buscar: \n"))
        cpfModificar = str(input("Digite o CPF para buscar: \n"))
        cliente_existe = BancoDadosController.buscarCliente(nomeModificar, cpfModificar)
        if cliente_existe is None:
            print("o cliente não existe!")
            input("pressione ENTER para continuar")
            return None
        else:
            nomeNovo = str(input("Digite o novo nome do cliente: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            telefone = str(input("Digite o telefone do novo cliente: \n"))
            endereco = EnderecoController.cadastrarEndereco()  # tem que criar um novo endereço, depois eu penso em outra solução
            cliente_novo = BancoDadosController.modificarCliente(cliente_existe, nomeNovo, cpfNovo, telefone, endereco)
            if cliente_novo:
                return f'o cliente {nomeNovo} foi Atualizado'
            else:
                return f'o cliente {nomeNovo} não foi Atualizado'
    
    def deletarCliente():
        try:
            BancoDadosController.deletarCliente(ClienteController.buscarCliente2())
            print("cliente deletado com sucesso!")
            input("pressione ENTER para continuar")
            return True
        except Exception as e:
            print("ocorreu um erro ao deletar o cliente: ", e)
            input("pressione ENTER para continuar")
            return False
        
            
            
        
        