import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController


class AtendenteController():
    
    @staticmethod
    def cadastrarAtendente():
        nome = str(input("Digite o nome do Cliente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        Atendente_existe = BancoDadosController.buscarAtendente(nome, cpf)
        if Atendente_existe is None:
            telefone = str(input("Digite o Telefone: \n"))
            endereco = EnderecoController.cadastrarEndereco()
            salario = float(input("Digite o Salário: \n"))
            BancoDadosController.cadastrarCliente(nome, cpf, telefone, endereco, salario)
            print("cadastro do Atendente sucedido!")
            input("pressione ENTER para continuar")
            return True
        else: 
            print("o Atendente já existe!")
            input("pressione ENTER para continuar")
            return False
    
    @staticmethod
    def buscarAtendente():
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarAtendente(nome, cpf) is None:
            print("o Atendente não existe!")
            input("pressione ENTER para continuar")
        else: 
            print(BancoDadosController.buscarAtendente(nome, cpf).__str__())
            input("pressione ENTER para continuar")
    
    @staticmethod
    def buscarAtendente2():
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarAtendente(nome, cpf) is None:
            return None
        else:
            return BancoDadosController.buscarAtendente(nome, cpf)
    
    @staticmethod
    def modificarAtendente():
        nomeModificar = str(input("Digite o nome do Atendente para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        Atendente_existe = BancoDadosController.buscarAtendente(nomeModificar, cpfModificar)
        if Atendente_existe is None:
            print("o Atendente não existe!")
            input("pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do Atendente: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            telefoneNovo = str(input("Digite o telefone: \n"))
            enderecoNovo = EnderecoController.cadastrarEndereco()
            salarioNovo = float(input("Digite o salário: \n"))
            try:
                BancoDadosController.modificarAtendente(Atendente_existe, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo)
                print(f'o Atendente {nomeNovo} foi Atualizado')
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print(f'o Atendente {nomeNovo} não foi Atualizado por erro: {e}')
                return False
    
    @staticmethod
    def deletarAtendente():
        try:
            Atendente_deletar =AtendenteController.buscarAtendente2()
            BancoDadosController.deletarAtendente(Atendente_deletar)
            print("Atendente deletado com sucesso")
            input("pressione ENTER para continuar")
            return True
        except Exception as e:
            print(f'Erro ao deletar o Atendente: {e}')
            input("pressione ENTER para continuar")
            return False