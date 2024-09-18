
import sys
sys.path.append('.')
from Controller.BancoDadosController import BancoDadosController
from Controller.ClienteController import ClienteController
from Controller.ConsultaController import ConsultaController
from Controller.EnderecoController import EnderecoController
import os
def clear():
    return os.system('cls')

class MenuViewMedico():
    
    def __init__(self):
        self.banco_dados_controller = BancoDadosController()
        self.endereco_controller = EnderecoController()
        self.cliente_controller = ClienteController(self.banco_dados_controller, self.endereco_controller)
        self.consulta_controller = ConsultaController(self.banco_dados_controller)
    
    def menuView(self):
        
        while True:
            
            print("""
                ----------------------------------------------------
                |Menu 1x    Menu 2x      Menu 3x       Menu 4x     | 
                |Cliente   Consulta      Medicos     Administrativo|
                ----------------------------------------------------  


12 - Buscar Cliente                         22 - Verificar histórico de consultas do cliente
13 - Modificar dados do cliente             23 - Modificar consulta (precisa do numero da consulta)
43 - Mostrar todos os clientes              24 - Cancelar consulta              
                                            25 - Buscar consulta por Número
                                            
31 - Gerar Receita (não implementado)       41 - Todas as Consultas agendadas   
32 - Gerar Atestado (não implementado)      42 - valor total do faturamento     
                                            43 - Mostrar todos os clientes
00 - Sair

                """)
            try:
                opcao = input("Digite o número correspondente ao menu: ").strip()
                opcao = int(opcao)
                match opcao:
                    case 12:
                        self.cliente_controller.buscarCliente()
                    case 13:
                        self.cliente_controller.modificarCliente()
                    case 22:
                        self.consulta_controller.buscarNumeroListaConsulta()
                    case 23:
                        self.consulta_controller.modificarConsulta()
                    case 24:
                        self.consulta_controller.deletarConsulta()
                    case 25:
                        self.consulta_controller.buscarConsulta()
                    case 41:
                        self.banco_dados_controller.mostrar_consultas()
                    case 42:
                        self.banco_dados_controller.valorTotalConsultas()
                    case 43:
                        self.banco_dados_controller.mostrarClientes()
                    case 00:
                        break
            except ValueError:
                print("Opção inválida")
                input("Pressione Enter para continuar")
                self.menuView()
                    
# if __name__ == "__main__":
    
#     menuview = MenuViewMedico()
#     menuview.menuView()