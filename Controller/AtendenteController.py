import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController


class AtendenteController():
    
    def __init__(self, banco_dados_controller):
        self.banco_dados_controller = banco_dados_controller
    
    def cadastrarAtendente(self):
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        Atendente_existe = self.banco_dados_controller.buscarAtendente(nome, cpf)
        if Atendente_existe is None:
            telefone = str(input("Digite o Telefone: \n"))
            endereco = EnderecoController.cadastrarEndereco()
            salario = float(input("Digite o Salário: \n"))
            self.banco_dados_controller.cadastrarAtendente(nome, cpf, telefone, endereco, salario)
            print("cadastro do Atendente sucedido!")
            input("pressione ENTER para continuar")
            return True
        else: 
            print("o Atendente já existe!")
            input("pressione ENTER para continuar")
            return False
    
    
    def buscarAtendente(self):
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if self.banco_dados_controller.buscarAtendente(nome, cpf) is None:
            print("o Atendente não existe!")
            input("pressione ENTER para continuar")
        else: 
            print(self.banco_dados_controller.buscarAtendente(nome, cpf).__str__())
            input("pressione ENTER para continuar")
    
    
    def buscarAtendente2(self):
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if self.banco_dados_controller.buscarAtendente(nome, cpf) is None:
            return None
        else:
            return self.banco_dados_controller.buscarAtendente(nome, cpf)
    
    
    def modificarAtendente(self):
        nomeModificar = str(input("Digite o nome do Atendente para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        Atendente_existe = self.banco_dados_controller.buscarAtendente(nomeModificar, cpfModificar)
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
                self.banco_dados_controller.modificarAtendente(Atendente_existe, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo)
                print(f'o Atendente {nomeNovo} foi Atualizado')
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print(f'o Atendente {nomeNovo} não foi Atualizado por erro: {e}')
                input("pressione ENTER para continuar")
                return False
    
    
    def deletarAtendente(self):
        try:
            Atendente_deletar =self.buscarAtendente2()
            self.banco_dados_controller.deletarAtendente(Atendente_deletar)
            print("Atendente deletado com sucesso")
            input("pressione ENTER para continuar")
            return True
        except Exception as e:
            print(f'Erro ao deletar o Atendente: {e}')
            input("pressione ENTER para continuar")
            return False