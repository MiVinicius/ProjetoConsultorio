import sys
sys.path.append('.')
from ProjetoConsultorio.Model.MedicoModel import Medico

class MedicoController():
    
    def __init__(self, banco_dados_controller, endereco_controller):
        self.banco_dados_controller = banco_dados_controller
        self.endereco_controller = endereco_controller
    
    def cadastrarMedico(self):
        try:
            nome = str(input("Digite o nome do Médico: \n")).strip()
            cpf = str(input("Digite o CPF: \n")).strip()
            cpf_limpo = Medico.validar_cpf(cpf)
            medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
            if medico_existe is None:
                print("Cadastrando o medico...")
                DataNasc = str(input("Digite a data de nascimento: \n"))
                telefone = str(input("Digite o telefone: \n"))
                endereco = self.endereco_controller.cadastrarEndereco()
                salario = float(input("Digite o salário: \n"))
                crm = str(input("Digite o CRM: \n"))
                self.banco_dados_controller.cadastrarMedico(nome, cpf_limpo, DataNasc, telefone, salario, crm, endereco)
                print("cadastro do médico sucedido!")
                input("pressione ENTER para continuar")
                return True
            else:
                print("o medico já existe!")
                input("pressione ENTER para continuar")
                return False
        except Exception as e: 
            print(f"cadastro do Médico falhou por erro: {e}")
            input("pressione ENTER para continuar")
            return False
    
    def buscarMedico(self):
        nome = str(input("Digite o nome do medico: \n")).strip()
        cpf = str(input("Digite o CPF: \n")).strip()
        cpf_limpo = Medico.validar_cpf(cpf)
        medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
        if medico_existe is None:  
            print("o medico não existe!")
            input("pressione ENTER para continuar")
        else: 
            input("pressione ENTER para continuar")
            
    
    def buscarMedico2(self):
        nome = str(input("Digite o nome do medico: \n")).strip()
        cpf = str(input("Digite o CPF: \n")).strip()
        cpf_limpo = Medico.validar_cpf(cpf)
        medico_existe = self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
        if medico_existe is None:
            return None
        else:
            return medico_existe
        
    def modificarMedico(self):
        nomeModificar = str(input("Digite o nome do médico para modificar: \n")).strip()
        cpfModificar = str(input("Digite o CPF para modificar: \n")).strip()
        cpf_limpo = Medico.validar_cpf(cpfModificar)
        medico_existe = self.banco_dados_controller.buscarMedico(nomeModificar, cpf_limpo)
        if medico_existe is None:
            print("O Médico não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            nomeNovo = str(input("Digite o novo nome do médico: \n")).strip()
            DataNascNovo = str(input("Digite a nova data de nascimento: \n"))
            telefoneNovo = str(input("Digite o telefone: \n"))
            salarioNovo = float(input("Digite o salário: \n"))
            crmNovo = str(input("Digite o CRM: \n"))
            try:
                self.banco_dados_controller.modificarMedico(medico_existe, nomeNovo, medico_existe.cpf, DataNascNovo, telefoneNovo, salarioNovo, crmNovo)
                print("O Médico foi Atualizado")
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print("O Médico não foi Atualizado, erro", e)
                input("pressione ENTER para continuar")
                return False
            
    def atualizarEndereco(self):
        nomeModificar = input("Digite o nome do Medico para buscar: \n").strip()
        cpfModificar = input("Digite o CPF para buscar: \n").strip()
        cpf_limpo = Medico.validar_cpf(cpfModificar)
        medico_existente = self.banco_dados_controller.buscarMedico(nomeModificar, cpf_limpo)
        if medico_existente is None:
            print("O Médico não existe!")
            input("Pressione ENTER para continuar")
            return False
        else:
            novoEndereco = self.endereco_controller.cadastrarEndereco()
            self.banco_dados_controller.atualizar_endereco(medico_existente, novoEndereco)
            print("Endereço atualizado com sucesso!")
            input("Pressione ENTER para continuar")
            return True

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