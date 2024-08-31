import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

class MedicoController():
    @staticmethod
    def cadastrarMedico():
        nome = str(input("Digite o nome do Médico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        medico_existe = BancoDadosController.buscarMedico(nome, cpf)
        if medico_existe is None:
            telefone = str(input("Digite o telefone: \n"))
            endereco = EnderecoController.cadastrarEndereco()
            salario = float(input("Digite o salário: \n"))
            crm = str(input("Digite o CRM: \n"))
            BancoDadosController.cadastrarMedico(nome, cpf, telefone, endereco, salario, crm)
            print("cadastro do médico sucedido!")
            input("pressione ENTER para continuar")
            return True
        else: 
            print("o medico já existe!")
            input("pressione ENTER para continuar")
            return False
    
    @staticmethod
    def buscarMedico():
        nome = str(input("Digite o nome do medico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        if BancoDadosController.buscarMedico(nome, cpf) is None:  
            print("o medico não existe!")
            input("pressione ENTER para continuar")
        else: 
            print(BancoDadosController.buscarMedico(nome, cpf).__str__())
            input("pressione ENTER para continuar")
            
    @staticmethod
    def buscarMedico2():
        nome = str(input("Digite o nome do medico: \n"))
        cpf = str(input("Digite o CPF: \n"))
        medico_existe = BancoDadosController.buscarMedico(nome, cpf)
        if medico_existe is None:
            return None
        else:
            return medico_existe
        
    
    @staticmethod
    def modificarMedico():
        nomeModificar = str(input("Digite o nome do cliente para modificar: \n"))
        cpfModificar = str(input("Digite o CPF para modificar: \n"))
        medico_existe = BancoDadosController.buscarMedico(nomeModificar, cpfModificar)
        if medico_existe is None:
            print("o medico não existe!")
            input("pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do cliente: \n"))
            cpfNovo = str(input("Digite o novo CPF: \n"))
            telefoneNovo = str(input("Digite o telefone: \n"))
            enderecoNovo = EnderecoController.cadastrarEndereco()
            salarioNovo = float(input("Digite o salário: \n"))
            crmNovo = str(input("Digite o CRM: \n"))
            try:
                BancoDadosController.modificarMedico(medico_existe, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo, crmNovo)
                print("o medico foi Atualizado")
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print("o medico não foi Atualizado, erro", e)
                input("pressione ENTER para continuar")
                return False

        
    
    @staticmethod
    def deletarMedico():
        try:
            medicoDeletar = MedicoController.buscarMedico2()
            BancoDadosController.deletarMedico(medicoDeletar)
            print("o medico foi excluído")
            input("pressione ENTER para continuar")
            return True
        except Exception as e:
            print("o medico não foi excluído, erro", e)
            input("pressione ENTER para continuar")
            return False