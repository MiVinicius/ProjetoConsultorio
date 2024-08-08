
from Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Controller.ClienteController import ClienteController
from ProjetoConsultorio.Controller.ConsultaController import consultaController

class FuncionarioController():
    
    @staticmethod
    def cadastrarFuncionario():
        funcionario = Funcionario(str(input("Digite o nome do Cliente: \n")), str(input("Digite o CPF: \n")))
        if BancoDadosController.buscarFuncionario(funcionario) is None:
            BancoDadosController.cadastrarCliente(funcionario)
            print("cadastro do funcionario sucedido!")
            return True
        else: 
            print("o funcionario já existe!")
            return False
    
    @staticmethod
    def cadastrarConsulta():
        while True:
            opcao = str(input("Já tem cadastro? Sim para continuar - Não para cadastrar "))
            if opcao == "sim":
                nome = str(input("Digite o nome do cliente para procurar: \n"))
                cpf = str(input("Digite o CPF do cliente para procurar: \n"))
                cliente = Cliente(nome, cpf)
                cliente_existente = BancoDadosController.buscarCliente(cliente)
                if cliente_existente:
                    consultaController.cadastrarConsulta(cliente_existente)
                    break
                else:
                    print("Cliente não encontrado. Por favor, tente novamente.")
            elif opcao == "não":
                ClienteController.cadastrarCliente()
                break
            else:
                print("Opção inválida. Por favor, responda 'Sim' ou 'Não'.")
                pass 
    
    @staticmethod
    def buscarFuncionario():
        funcionario = Funcionario(str(input("Digite o nome do funcionario: \n")), str(input("Digite o CPF: \n")))
        return BancoDadosController.buscarFuncionario(funcionario)
    
    @staticmethod
    def modificarFuncionario():
        funcionario = Funcionario(str(input("Digite o nome do funcionario: \n")), str(input("Digite o CPF: \n")))
        funcionario_novo = Funcionario(str(input("Digite o novo nome do funcionario: \n")), str(input("Digite o novo CPF: \n")))
        return BancoDadosController.modificarFuncionario(BancoDadosController.buscarFuncionario(funcionario), funcionario_novo)
    
    @staticmethod
    def deletarFuncionario():
        return BancoDadosController.deletarFuncionario(FuncionarioController.buscarFuncionario())