import sys
from ProjetoConsultorio.Model.AtendenteModel import Atendente
sys.path.append('.')


class AtendenteController():
    
    def __init__(self, banco_dados_controller, endereco_controller):
        self.banco_dados_controller = banco_dados_controller
        self.endereco_controller = endereco_controller
    
    def cadastrarAtendente(self):
        try:
            nome = str(input("Digite o nome do Atendente: \n")).strip()
            cpf = str(input("Digite o CPF: \n")).strip()
            cpf_limpo = Atendente.validar_cpf(cpf)
            Atendente_existe = self.banco_dados_controller.buscarAtendente(nome, cpf_limpo)
            if Atendente_existe is None:
                print("Cadastrando o Atendente...")            
                DataNasc = str(input("Digite a Data de Nascimento: \n"))
                telefone = str(input("Digite o Telefone: \n"))
                endereco = self.endereco_controller.cadastrarEndereco()
                salario = float(input("Digite o Salário: \n"))
                self.banco_dados_controller.cadastrarAtendente(nome, cpf, DataNasc, telefone, salario, endereco)
                print("cadastro do Atendente sucedido!")
                input("pressione ENTER para continuar")
                return True
            else: 
                print("o Atendente já existe!")
                input("pressione ENTER para continuar")
                return False
        except Exception as e:
                print("cadastro do Atendente falhou, erro", e)
                input("pressione ENTER para continuar")
                return False
    
    
    def buscarAtendente(self):
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        cpf_limpo = Atendente.validar_cpf(cpf)
        atendente_existe = self.banco_dados_controller.buscarAtendente(nome, cpf_limpo)
        if atendente_existe is None:
            print("o Atendente não existe!")
            input("pressione ENTER para continuar")
        else:
            input("pressione ENTER para continuar")
    
    
    def buscarAtendente2(self):
        nome = str(input("Digite o nome do Atendente: \n"))
        cpf = str(input("Digite o CPF: \n"))
        cpf_limpo = Atendente.validar_cpf(cpf)
        atendente_existe = self.banco_dados_controller.buscarAtendente(nome, cpf_limpo)
        if atendente_existe is None:
            return None
        else:
            return atendente_existe
    
    
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
            DataNasc = str(input("Digite a nova Data de Nascimento: \n"))
            telefoneNovo = str(input("Digite o telefone: \n"))
            salarioNovo = float(input("Digite o salário: \n"))
            try:
                self.banco_dados_controller.modificarAtendente(Atendente_existe, nomeNovo, Atendente_existe.cpf, DataNasc, telefoneNovo, salarioNovo)
                print(f'o Atendente {nomeNovo} foi Atualizado')
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print(f'o Atendente {nomeNovo} não foi Atualizado por erro: {e}')
                input("pressione ENTER para continuar")
                return False
            
    def atualizarEndereco(self):
        nomeModificar = input("Digite o nome do Atendente para buscar: \n").strip()
        cpfModificar = input("Digite o CPF para buscar: \n").strip()
        cpf_limpo = Atendente.validar_cpf(cpfModificar)
        atendente_existente: Atendente = self.banco_dados_controller.buscarAtendente(nomeModificar, cpf_limpo)
        if atendente_existente is None:
            print("O Atendente não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            novoEndereco = self.endereco_controller.cadastrarEndereco()
            try:
                enderecoAntigo = atendente_existente.endereco_id
                enderecoAtualizar = self.banco_dados_controller.atualizar_endereco(enderecoAntigo, novoEndereco)
                if enderecoAtualizar:
                    print("Endereço atualizado com sucesso!")
                    input("Pressione ENTER para continuar")
                    return True
                else:
                    print("Erro ao atualizar o endereço.")
                    input("Pressione ENTER para continuar")
            except Exception as e:
                print("Ocorreu um erro ao atualizar o endereço:", e)
                input("Pressione ENTER para continuar")
    
    
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