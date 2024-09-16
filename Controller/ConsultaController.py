import sys
sys.path.append('.')

from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico



class ConsultaController():
    
    def __init__(self, banco_dados_controller):
        self.banco_dados_controller = banco_dados_controller
    
    # Create
    
    def cadastrarConsulta(self):
        while True:
            opcao = input("O cliente já tem cadastro? S para continuar - N para cadastrar! \n").lower()  # Assim não tem problema de digitar S maiúsculo
            if opcao == "s":
                nome = input("Digite o nome do cliente para procurar: \n").strip()
                cpf = input("Digite o CPF do cliente para procurar: \n").strip()
                cpf_limpo = Cliente.validar_cpf(cpf)
                cliente_existente = self.banco_dados_controller.buscarCliente(nome, cpf_limpo)
                if cliente_existente:
                    self.cadastrarConsulta2(cliente_existente)
                    break
                else:
                    print("Cliente não encontrado. Por favor, tente novamente.")
                    input("Pressione ENTER para continuar")
                    break
            elif opcao == "n":
                print("Cadastre um novo cliente!")
                input("Pressione ENTER para continuar")
                break
            else:
                print("Opção inválida. Por favor, responda 's' ou 'n'.")
    
    def cadastrarConsulta2(self, cliente: Cliente):
        descricao = str(input("Digite a descrição da consulta: \n"))
        data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
        horario = str(input("Digite o horário da consulta (hh:mm): \n"))
        valor = float(input("Digite o valor da consulta: \n"))
        medico = self.buscarMedicoConsulta()
        if medico is None:
            print("Medico inexistente") 
            input("pressione ENTER para continuar")
            return False
        if self.banco_dados_controller.cadastrarConsulta(descricao, data, horario, valor, cliente.cpf, medico.crm):
            print(f"Consulta adicionada para o cliente {cliente.nome}")
            input("pressione ENTER para continuar")
            return True
        return False

    # Retrieve

    def buscarClienteConsulta(self):  
        nome = input("Digite o nome do cliente para procurar: \n").strip()
        cpf = input("Digite o CPF do cliente para procurar: \n").strip()
        cpf_limpo = Cliente.validar_cpf(cpf)
        return self.banco_dados_controller.buscarCliente(nome, cpf_limpo)
    
    def buscarMedicoConsulta(self):
        nome = input("Digite o nome do medico para procurar: \n").strip()
        cpf = input("Digite o CPF do medico para procurar: \n").strip()
        cpf_limpo = Medico.validar_cpf(cpf)
        return self.banco_dados_controller.buscarMedico(nome, cpf_limpo)
    
    def buscarNumeroListaConsulta(self):
        numero = int(input("Digite o número do CPF do CLiente para procurar as consultas: \n"))
        lista = self.banco_dados_controller.buscarListaConsulta(numero)
        print("Consultas:")
        for consulta in lista:
            print(consulta)  
            print()
        input("pressione ENTER para continuar")
        return
        
    def buscarConsulta(self):
        numero = int(input("Digite o número da consulta para procurar: \n"))
        consulta = self.banco_dados_controller.buscarConsulta(numero)
        if consulta is not None:
            print(consulta)
            input("pressione ENTER para continuar")
            return consulta
        else:
            print("consulta inexistente")
            input("pressione ENTER para continuar")
            return None

    # Update

    def modificarConsulta(self):
        consultaModificar = self.buscarConsulta()
        if consultaModificar is not None:
            descricao = str(input("Digite a nova descrição da consulta: \n"))
            data = str(input("Digite a nova data da consulta (dd/mm/yyyy): \n"))
            horario = str(input("Digite o novo horário da consulta (hh:mm): \n"))
            valor = float(input("Digite o novo valor da consulta: \n"))
            medico = self.buscarMedicoConsulta()
            try:
                consulta = self.banco_dados_controller.modificarConsulta(descricao, data, horario, valor, None, medico.crm, consultaModificar)
                if consulta is not None:
                    print("consulta modificada com sucesso!")
                    input("pressione ENTER para continuar")
                    return True
                else:
                    print("consulta não foi modificada!")
                    input("pressione ENTER para continuar")
                    return False
            except Exception as e:
                print("Consulta não foi modificada, erro:", e)
                input("pressione ENTER para continuar")
        else:
            print("consulta inexistente")
            return False
        
    # Delete
    
    def deletarConsulta(self):
        cliente = self.buscarClienteConsulta()
        if cliente:
            consulta = self.buscarConsulta()
            if consulta:
                self.banco_dados_controller.deletarConsulta(consulta)
                print("consulta deletada com sucesso!")
                input("pressione ENTER para continuar")
                return True
            else:
                print("consulta inexistente")
                input("pressione ENTER para continuar")
                return False
        else:
            print("consulta inexistente")
            input("pressione ENTER para continuar")
            return False
            