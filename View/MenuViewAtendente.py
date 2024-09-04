import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController
from ProjetoConsultorio.Controller.ConsultaController import ConsultaController
import os

def clear():
    return os.system('cls')

class MenuViewAtendente():
    
    def __init__(self):
        self.banco_dados_controller = BancoDadosController()
        self.cliente_controller = ClienteController(self.banco_dados_controller)
        self.consulta_controller = ConsultaController(self.banco_dados_controller)
    
    def menuView(self):
        
        while True:
            
            print("""
                ----------------------------------------------------
                |Menu 1x    Menu 2x      Menu 3x       Menu 4x     | 
                |Cliente   Consulta    Atendentes  Administrativo  |
                ----------------------------------------------------  

11 - Cadastrar Cliente			    21 - Agendar consulta
12 - Buscar Cliente			    22 - Verificar histórico de consultas do cliente
13 - Modificar dados do cliente		    23 - Modificar consulta (precisa do numero da consulta)
14 - Remover cliente 			    24 - Cancelar consulta

41 - Todas as Consultas agendadas
45 - Mostrar todos os médicos
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
                    case 21:
                        self.consulta_controller.cadastrarConsulta()
                    case 22:
                        self.consulta_controller.buscarNumeroListaConsulta()
                    case 23:
                        self.consulta_controller.modificarConsulta()
                    case 24:
                        self.consulta_controller.deletarConsulta()
                    case 41:
                        self.banco_dados_controller.mostrar_consultas()
                    case 45:
                        self.banco_dados_controller.mostrarMedicos()
                    case 00:
                        break
            except ValueError:
                print("Opção inválida")
                input("Pressione Enter para continuar")
                self.menuView()
                    
# if __name__ == "__main__":
    
#     menuview = MenuViewAtendente()
#     menuview.menuView()