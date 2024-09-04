import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

class MedicoController():
    
    def __init__(self, banco_dados_controller):
        self.banco_dados_controller = banco_dados_controller
    
    def cadastrarMedico(self):
        nome = str(input("Digite o nome do Médico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf)
        if medico_existe is None:
            telefone = str(input("Digite o telefone: \n"))
            endereco = EnderecoController.cadastrarEndereco()
            salario = float(input("Digite o salário: \n"))
            crm = str(input("Digite o CRM: \n"))
            try:
                self.banco_dados_controller.cadastrarMedico(nome, cpf, telefone, endereco, salario, crm)
                print("cadastro do médico sucedido!")
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print(f"cadastro do usuário falhou por erro: {e}")
                input("pressione ENTER para continuar")
                return False
        else: 
            print("o medico já existe!")
            input("pressione ENTER para continuar")
            return False
    
    
    def buscarMedico(self):
        nome = str(input("Digite o nome do medico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if self.banco_dados_controller.buscarMedico(nome, cpf) is None:  
            print("o medico não existe!")
            input("pressione ENTER para continuar")
        else: 
            print(self.banco_dados_controller.buscarMedico(nome, cpf).__str__())
            input("pressione ENTER para continuar")
            
    
    def buscarMedico2(self):
        nome = str(input("Digite o nome do medico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf)
        if medico_existe is None:
            return None
        else:
            return medico_existe
        
    
    
    def modificarMedico(self):
        nomeModificar = str(input("Digite o nome do médico para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        medico_existe = self.banco_dados_controller.buscarMedico(nomeModificar, cpfModificar)
        if medico_existe is None:
            print("o medico não existe!")
            input("pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do médico: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            telefoneNovo = str(input("Digite o telefone: \n"))
            enderecoNovo = EnderecoController.cadastrarEndereco()
            salarioNovo = float(input("Digite o salário: \n"))
            crmNovo = str(input("Digite o CRM: \n"))
            try:
                self.banco_dados_controller.modificarMedico(medico_existe, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo, crmNovo)
                print("o medico foi Atualizado")
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print("o medico não foi Atualizado, erro", e)
                input("pressione ENTER para continuar")
                return False

        
    
    
    def deletarMedico(self):
        try:
            medicoDeletar = self.buscarMedico2()
            self.banco_dados_controller.deletarMedico(medicoDeletar)
            print("o medico foi excluído")
            input("pressione ENTER para continuar")
            return True
        except Exception as e:
            print("o medico não foi excluído, erro", e)
            input("pressione ENTER para continuar")
            return False