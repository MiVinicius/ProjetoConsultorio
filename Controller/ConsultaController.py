import sys
sys.path.append('.')

from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController


class ConsultaController():
    
    
    # Create
    
    def cadastrarConsulta():
        while True:
            opcao = str(input("O cliente já tem cadastro? S para continuar - N para cadastrar! \n"))
            if opcao == "s" or "S":
                nome = str(input("Digite o nome do cliente para procurar: \n"))
                cpf = str(input("Digite o CPF do cliente para procurar: \n"))
                cliente_existente = BancoDadosController.buscarCliente(nome, cpf)
                if cliente_existente:
                    ConsultaController.cadastrarConsulta2(cliente_existente)
                    break
                else:
                    print("Cliente não encontrado. Por favor, tente novamente.")
                    ConsultaController.cadastrarConsulta()
            elif opcao == "n" or "N":
                ClienteController.cadastrarCliente()
                break
            else:
                print("Opção inválida. Por favor, responda 's' ou 'n'.")
                pass 
    
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

    def buscarClienteConsulta():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF do cliente para procurar: \n"))
        return BancoDadosController.buscarCliente(nome, cpf)

    
    def buscarNumeroListaConsulta():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF do cliente para procurar: \n"))
        return BancoDadosController.buscarCliente(nome, cpf)._getConsulta()
    
    
    def buscarConsulta():
        numero = int(input("Digite o número da consulta para procurar: \n"))
        consulta = BancoDadosController.buscarConsulta(numero)
        if consulta is not None:
            print(consulta.__str__())
            input("pressione ENTER para continuar")
            return consulta
        else:
            print("consulta inexistente")
            input("pressione ENTER para continuar")
            return None
    
    
    # def buscarConsulta2():
    #     numero = int(input("Digite o número da consulta para procurar: \n"))
    #     return BancoDadosController.buscarConsulta(numero)
    
    
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
    
    def deletarConsulta2():
        cliente = ConsultaController.buscarClienteConsulta()
        if cliente:
            consulta = ConsultaController.buscarConsulta()._getNumero()
            if consulta:
                cliente._getConsulta().remove(consulta)
                BancoDadosController.deletarConsulta(consulta)
                return True
            else:
                print("consulta inexistente")
                return False
            
    
if __name__ == "__main__":
    caos = ConsultaController()
    caos.cadastrarConsulta()
    # caos.buscarConsulta()