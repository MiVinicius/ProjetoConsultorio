import sys
sys.path.append('.')

from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController

class ConsultaController():
    
    @staticmethod
    def cadastrar():
        while True:
            opcao = str(input("Já tem cadastro? S para continuar - N para cadastrar! \n"))
            if opcao == "s" or "S":
                nome = str(input("Digite o nome do cliente para procurar: \n"))
                cpf = str(input("Digite o CPF do cliente para procurar: \n"))
                cliente_existente = BancoDadosController.buscarCliente(nome, cpf)
                if cliente_existente:
                    ConsultaController.cadastrarConsulta(cliente_existente)
                    break
                else:
                    print("Cliente não encontrado. Por favor, tente novamente.")
                    ConsultaController.cadastrar()
            elif opcao == "n" or "N":
                ClienteController.cadastrarCliente()
                buscarCliente = ClienteController.buscarCliente2()
                if buscarCliente:
                    ConsultaController.cadastrarConsulta(buscarCliente)
                break
            else:
                print("Opção inválida. Por favor, responda 's' ou 'n'.")
                pass 
    
    def cadastrarConsulta(cliente: Cliente):
        descricao = str(input("Digite a descrição da consulta: \n"))
        data = str(input("Digite a data da consulta (dd/mm/yyyy): \n"))
        if BancoDadosController.cadastrarConsulta(descricao, data, cliente):
            print(f"Consulta adicionada para o cliente {cliente._getNome()}")
            input("pressione ENTER para continuar")
            return True
        return False

    @staticmethod
    def buscarConsulta():
        nome = str(input("Digite o nome do cliente para procurar: \n"))
        cpf = str(input("Digite o CPF do cliente para procurar: \n"))
        return BancoDadosController.buscarCliente(nome, cpf)._getConsulta()
    
    
    @staticmethod
    def buscarConsulta2():
        numero = int(input("Digite o número da consulta para procurar: \n"))
        return BancoDadosController.buscarConsulta(numero)
    
    def modificarConsulta():
        consultaModificar = ConsultaController.buscarConsulta2()
        if consultaModificar is not None:
            descricao = str(input("Digite a nova descrição da consulta: \n"))
            data = str(input("Digite a nova data da consulta (dd/mm/yyyy): \n"))
            return BancoDadosController.modificarConsulta(descricao, data, consultaModificar, cliente=None)
        else:
            print("consulta inexistente")
            return False
        
        
    # def modificarConsulta2():
    #     cliente = ClienteController.buscarCliente()
    #     if cliente is not None:
    #         descricao = str(input("Digite a nova descrição da consulta: \n"))
    #         data = str(input("Digite a nova data da consulta (dd/mm/yyyy): \n"))
    #         return BancoDadosController.modificarConsulta2(descricao, data, cliente)
    #     else:
    #         print("consulta inexistente")
    #         return False
    
            
    def deletarConsulta():
        consulta = ConsultaController.buscarConsulta2()
        if consulta:
            return BancoDadosController.deletarConsulta(consulta)
    
    # def deletarConsulta2():
    #     pass
    
if __name__ == "__main__":
    caos = ConsultaController()
    caos.cadastrar()
    # caos.buscarConsulta()