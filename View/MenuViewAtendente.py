import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController
from ProjetoConsultorio.Controller.ConsultaController import ConsultaController
import os
from ProjetoConsultorio.Controller.EnderecoController import EnderecoController

def clear():
    return os.system('cls')

class MenuViewAtendente():
    
    def __init__(self):
        self.banco_dados_controller = BancoDadosController()
        self.endereco_controller = EnderecoController()
        self.cliente_controller = ClienteController(self.banco_dados_controller, self.endereco_controller)
        self.consulta_controller = ConsultaController(self.banco_dados_controller)
    
    def menuView(self):
        
        while True:
            
            print("""
                -----------------------------------------
                |Menu 1x    Menu 2x      Menu 3x        | 
                |Cliente   Consulta     Administrativo  |
                ----------------------------------------- 

11 - Cadastrar Cliente			        21 - Agendar consulta
12 - Buscar Clientes			        22 - Verificar histórico de consultas do cliente
13 - Modificar dados do cliente                 23 - Modificar consulta (precisa do numero da consulta)
14 - Remover cliente 			        24 - Cancelar consulta
15 - Alterar endereço do cliente                25 - Buscar consulta por Número

31 - Todas as Consultas agendadas
32 - Mostrar todos os Médicos
33 - Mostrar todos os Clientes

00 - Sair

                """)
            try:
                opcao = input("Digite o número correspondente ao menu: ").strip()
                opcao = int(opcao)
                match opcao:
                    case 11:
                        self.cliente_controller.cadastrarCliente()  
                    case 12:
                        self.cliente_controller.buscarCliente()
                    case 13:
                        self.cliente_controller.modificarCliente()
                    case 14:
                        self.cliente_controller.deletarCliente()
                    case 15:
                        self.cliente_controller.atualizarEndereco()
                    case 21:
                        self.consulta_controller.cadastrarConsulta()
                    case 22:
                        self.consulta_controller.buscarNumeroListaConsulta()
                    case 23:
                        self.consulta_controller.modificarConsulta()
                    case 24:
                        self.consulta_controller.deletarConsulta()
                    case 25:
                        self.consulta_controller.buscarConsulta()
                    case 31:
                        self.banco_dados_controller.mostrar_consultas()
                    case 32:
                        self.banco_dados_controller.mostrarMedicos()
                    case 33:
                        self.banco_dados_controller.mostrarClientes()
                    case 00:
                        break
            except ValueError:
                print("Opção inválida")
                input("Pressione Enter para continuar")
                self.menuView()
                    
# if __name__ == "__main__":
    
#     menuview = MenuViewAtendente()
#     menuview.menuView()