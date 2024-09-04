import sys
sys.path.append('.')

from ProjetoConsultorio.Model.ClienteModel import Cliente



class ConsultaController():
    
    def __init__(self, banco_dados_controller):
        self.banco_dados_controller = banco_dados_controller
    
    # Create
    
    def cadastrarConsulta(self):
        while True:
            opcao = input("O cliente já tem cadastro? S para continuar - N para cadastrar! \n").lower()  # Assim não tem problema de digitar S maiúsculo
            if opcao == "s":
                nome = input("Digite o nome do cliente para procurar: \n")
                cpf = input("Digite o CPF do cliente para procurar: \n")
                cliente_existente = self.banco_dados_controller.buscarCliente(nome, cpf)
                if cliente_existente:
                    self.cadastrarConsulta2(cliente_existente)
                    break
                else:
                    print("Cliente não encontrado. Por favor, tente novamente.")
                    input("Pressione ENTER para continuar")
                    break
            elif opcao == "n":
                self.cadastrarCliente()
                break
            else:
                print("Opção inválida. Por favor, responda 's' ou 'n'.")

    
    def cadastrarConsulta2(self, cliente: Cliente):
        descricao = str(input("Digite a descrição da consulta: \n"))
        data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
        horario = str(input("Digite o horário da consulta (hh:mm): \n"))
        valor = float(input("Digite o valor da consulta: \n"))
        if self.banco_dados_controller.cadastrarConsulta(descricao, data, horario, valor, cliente.cpf):
            print(f"Consulta adicionada para o cliente {cliente.nome}")
            input("pressione ENTER para continuar")
            return True
        return False

    # Retrieve

    def buscarClienteConsulta(self):  # isso aqui eu acho que deveria não estar aqui
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF do cliente para procurar: \n"))
        return self.banco_dados_controller.buscarCliente(nome, cpf)

    
    def buscarNumeroListaConsulta(self):
        lista = self.buscarClienteConsulta().consulta
        print("Consultas:")
        for consulta in lista:
            print(self.banco_dados_controller.buscarConsulta(consulta))  # funciona!
            print()
        input("pressione ENTER para continuar")
        
    
    
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
            return self.banco_dados_controller.modificarConsulta(descricao, data, horario, valor, consultaModificar)
        else:
            print("consulta inexistente")
            return False
        
        
    # Delete
    
    def deletarConsulta(self):
        cliente = self.buscarClienteConsulta()
        if cliente:
            consulta = self.buscarConsulta()
            if consulta:
                cliente.consulta.remove(consulta.numero)
                self.banco_dados_controller.deletarConsulta(consulta.numero)
                print("consulta deletada com sucesso!")
                input("pressione ENTER para continuar")
                return True
            else:
                print("consulta inexistente")
                return False
        else:
            print("consulta inexistente")
            return False
            
    
if __name__ == "__main__":
    caos = ConsultaController()
    caos.cadastrarConsulta()
    # caos.buscarConsulta()