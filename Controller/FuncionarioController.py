
import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController


class FuncionarioController():
    
    @staticmethod
    def cadastrarFuncionario():
        nome = str(input("Digite o nome do Cliente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        funcionario_existe = BancoDadosController.buscarFuncionario(nome, cpf)
        if funcionario_existe is None:
            telefone = str(input("Digite o Telefone: \n"))
            endereco = EnderecoController.cadastrarEndereco()
            salario = float(input("Digite o Salário: \n"))
            BancoDadosController.cadastrarCliente(nome, cpf, telefone, endereco, salario)
            print("cadastro do funcionario sucedido!")
            input("pressione ENTER para continuar")
            return True
        else: 
            print("o funcionario já existe!")
            input("pressione ENTER para continuar")
            return False
    
    @staticmethod
    def buscarFuncionario():
        nome = str(input("Digite o nome do funcionario: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarFuncionario(nome, cpf) is None:
            print("o funcionario não existe!")
            input("pressione ENTER para continuar")
        else: 
            print(BancoDadosController.buscarFuncionario(nome, cpf).__str__())
            input("pressione ENTER para continuar")
    
    @staticmethod
    def buscarFuncionario2():
        nome = str(input("Digite o nome do funcionario: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarFuncionario(nome, cpf) is None:
            return None
        else:
            return BancoDadosController.buscarFuncionario(nome, cpf)
    
    @staticmethod
    def modificarFuncionario():
        nomeModificar = str(input("Digite o nome do funcionario para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        if BancoDadosController.buscarFuncionario(nomeModificar, cpfModificar) is None:
            print("o funcionario não existe!")
            input("pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do Funcionario: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            if BancoDadosController.modificarFuncionario(BancoDadosController.buscarFuncionario(nomeModificar, cpfModificar), nomeNovo, cpfNovo):
                return f'o Funcionario {nomeNovo} foi Atualizado'
            else:
                return f'o Funcionario {nomeNovo} não foi Atualizado'
    
    @staticmethod
    def deletarFuncionario():
        return BancoDadosController.deletarFuncionario(FuncionarioController.buscarFuncionario2())