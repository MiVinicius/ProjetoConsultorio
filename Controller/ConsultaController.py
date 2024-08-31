import sys
sys.path.append('.')

from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController


class ConsultaController():
    
    
    # Create
    
    def cadastrarConsulta():
        while True:
            opcao = input("O cliente já tem cadastro? S para continuar - N para cadastrar! \n").lower()  # Assim não tem problema de digitar S maiúsculo
            if opcao == "s":
                nome = input("Digite o nome do cliente para procurar: \n")
                cpf = input("Digite o CPF do cliente para procurar: \n")
                cliente_existente = BancoDadosController.buscarCliente(nome, cpf)
                if cliente_existente:
                    ConsultaController.cadastrarConsulta2(cliente_existente)
                    break
                else:
                    print("Cliente não encontrado. Por favor, tente novamente.")
                    input("Pressione ENTER para continuar")
                    break
            elif opcao == "n":
                ClienteController.cadastrarCliente()
                break
            else:
                print("Opção inválida. Por favor, responda 's' ou 'n'.")

    
    def cadastrarConsulta2(cliente: Cliente):
        descricao = str(input("Digite a descrição da consulta: \n"))
        data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
        horario = str(input("Digite o horário da consulta (hh:mm): \n"))
        valor = float(input("Digite o valor da consulta: \n"))
        if BancoDadosController.cadastrarConsulta(descricao, data, horario, valor, cliente._getCpf()):
            print(f"Consulta adicionada para o cliente {cliente._getNome()}")
            input("pressione ENTER para continuar")
            return True
        return False

    # Retrieve

    def buscarClienteConsulta():  # isso aqui eu acho que deveria não estar aqui
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF do cliente para procurar: \n"))
        return BancoDadosController.buscarCliente(nome, cpf)

    
    def buscarNumeroListaConsulta():
        lista = ConsultaController.buscarClienteConsulta()._getConsulta()
        print("Consultas:")
        for consulta in lista:
            print(BancoDadosController.buscarConsulta(consulta))  # funciona!
            print()
        input("pressione ENTER para continuar")
        
    
    
    def buscarConsulta():
        numero = int(input("Digite o número da consulta para procurar: \n"))
        consulta = BancoDadosController.buscarConsulta(numero)
        if consulta is not None:
            print(consulta)
            input("pressione ENTER para continuar")
            return consulta
        else:
            print("consulta inexistente")
            input("pressione ENTER para continuar")
            return None


    # Update
    
    def modificarConsulta():
        consultaModificar = ConsultaController.buscarConsulta()
        if consultaModificar is not None:
            descricao = str(input("Digite a nova descrição da consulta: \n"))
            data = str(input("Digite a nova data da consulta (dd/mm/yyyy): \n"))
            horario = str(input("Digite o novo horário da consulta (hh:mm): \n"))
            valor = float(input("Digite o novo valor da consulta: \n"))
            return BancoDadosController.modificarConsulta(descricao, data, horario, valor, consultaModificar)
        else:
            print("consulta inexistente")
            return False
        
        
    # Delete
    
    def deletarConsulta():
        cliente = ConsultaController.buscarClienteConsulta()
        if cliente:
            consulta = ConsultaController.buscarConsulta()._getNumero()
            if consulta:
                
                BancoDadosController.deletarConsulta(consulta)
                cliente._getConsulta().remove(consulta)
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