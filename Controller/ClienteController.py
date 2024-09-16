import sys
from ProjetoConsultorio.Model.ClienteModel import Cliente
sys.path.append('.')

class ClienteController:
    
    def __init__(self, banco_dados_controller, endereco_controller):
        self.banco_dados_controller = banco_dados_controller
        self.endereco_controller = endereco_controller
    
    def cadastrarCliente(self):
        try:
            nome = input("Digite o nome do novo Cliente: \n").strip()
            cpf = input("Digite o CPF do novo cliente: \n").strip()
            cpf_limpo = Cliente.validar_cpf(cpf)
            cliente_existe = self.banco_dados_controller.buscarCliente(nome, cpf_limpo)
            if cliente_existe is None:
                print("Cadastrando o cliente...")
                dataNasc = input("Digite a data de nascimento do novo cliente: \n")
                telefone = input("Digite o telefone do novo cliente: \n")
                endereco = self.endereco_controller.cadastrarEndereco() 
                self.banco_dados_controller.cadastrarCliente(nome, cpf, dataNasc, telefone, endereco)
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
        nome = input("Digite o nome do cliente para procurar: \n").strip()
        cpf = input("Digite o CPF para procurar: \n").strip()
        cpf_limpo = Cliente.validar_cpf(cpf)
        cliente_existe = self.banco_dados_controller.buscarCliente(nome, cpf_limpo)
        if cliente_existe is None:
            print("O cliente não existe!")
            input("Pressione ENTER para continuar")
        else:
            input("Pressione ENTER para continuar")
        
    def buscarCliente2(self):
        nome = input("Digite o nome do cliente para procurar: \n").strip()
        cpf = input("Digite o CPF para procurar: \n").strip()
        cpf_limpo = Cliente.validar_cpf(cpf)
        return self.banco_dados_controller.buscarCliente(nome, cpf_limpo)
        
    def modificarCliente(self):
        nomeModificar = input("Digite o nome do cliente para buscar: \n").strip()
        cpfModificar = input("Digite o CPF para buscar: \n").strip()
        cpf_limpo = Cliente.validar_cpf(cpfModificar)
        cliente_existe = self.banco_dados_controller.buscarCliente(nomeModificar, cpf_limpo)
        if cliente_existe is None:
            print("O cliente não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            print("Atualizando o cliente...")
            nomeNovo = input("Digite o novo nome do cliente: \n")
            dataNasc = input("Digite a nova data de nascimento do cliente no formato dd/mm/yyyy: \n")
            telefone = input("Digite o novo telefone do cliente (xx) xxxxx-xxxx: \n")
            cliente_novo = self.banco_dados_controller.modificarCliente(cliente_existe, nomeNovo, cliente_existe.cpf, dataNasc, telefone)
            if cliente_novo:
                print(f"O cliente {nomeNovo} foi atualizado com sucesso!")
                input("Pressione ENTER para continuar")
                return True
            else:
                print("Ocorreu um erro ao atualizar o cliente")
                input("Pressione ENTER para continuar")
                return False
            
    def atualizarEndereco(self):
        nomeModificar = input("Digite o nome do cliente para buscar: \n").strip()
        cpfModificar = input("Digite o CPF para buscar: \n").strip()
        cpf_limpo = Cliente.validar_cpf(cpfModificar)
        cliente_existe = self.banco_dados_controller.buscarCliente(nomeModificar, cpf_limpo)
        if cliente_existe is None:
            print("O cliente não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            novoEndereco = self.endereco_controller.cadastrarEndereco()
            self.banco_dados_controller.atualizar_endereco(cliente_existe, novoEndereco)
            print("Endereço atualizado com sucesso!")
            input("Pressione ENTER para continuar")
            return True
    
    def deletarCliente(self):
        try:
            clienteDeletar = self.buscarCliente2()
            if clienteDeletar is None:
                print("O cliente não existe!")
                input("Pressione ENTER para continuar")
                return False
            self.banco_dados_controller.deletarCliente(clienteDeletar)
            print("Cliente deletado com sucesso!")
            input("Pressione ENTER para continuar")
            return True
        except Exception as e:
            print("Ocorreu um erro ao deletar o cliente:", e)
            input("Pressione ENTER para continuar")
            return False


            
            
        
        