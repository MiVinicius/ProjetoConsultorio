import sys
sys.path.append('.')
from Controller.ClienteController import ClienteController
from Controller.ConsultaController import ConsultaController
from Controller.MedicoController import MedicoController
from Controller.AtendenteController import AtendenteController
from Controller.BancoDadosController import BancoDadosController
from Controller.EnderecoController import EnderecoController
import os
def clear():
    return os.system('cls')

class MenuView:
    def __init__(self):  
        self.endereco_controller = EnderecoController()
        self.banco_dados_controller = BancoDadosController()
        self.consulta_controller = ConsultaController(self.banco_dados_controller)
        self.cliente_controller = ClienteController(self.banco_dados_controller, self.endereco_controller)
        self.medico_controller = MedicoController(self.banco_dados_controller, self.endereco_controller)
        self.atendente_controller = AtendenteController(self.banco_dados_controller, self.endereco_controller)
        

    def menuView(self):
        clear()
        while True:
            print("""
                ----------------------------------------------------
                |Menu 1x    Menu 2x      Menu 3x       Menu 4x     | 
                |Cliente   Consulta    Atendentes  Administrativo  |
                ----------------------------------------------------  

11 - Cadastrar Cliente                  21 - Agendar consulta
12 - Buscar Cliente                     22 - Verificar histórico de consultas do cliente
13 - Modificar dados do cliente         23 - Modificar consulta (precisa do numero da consulta)
14 - Remover cliente                    24 - Cancelar consulta (precisa do numero da consulta)
15 - Alterar endereço do cliente        25 - Buscar consulta por Número

31 - Cadastrar Médico                   41 - Todas as Consultas agendadas
32 - Cadastrar Atendente                42 - valor total do faturamento das consultas agendadas
33 - Buscar Médico                      43 - Mostrar todos os Atendentes
34 - Buscar Atendente                   44 - Mostrar todos os clientes
35 - Modificar dados de Médico          45 - Mostrar todos os médicos
36 - Modificar dados de Atendente       46 - Alterar endereco (Médico)
37 - Remover Médico                     47 - Alterar endereço (Atendente)
38 - Remover Atendente                  48 - Gerar Receita (não implementado)
00 - Sair                               49 - Gerar Atestado (não implementado)


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
                        self.medico_controller.cadastrarMedico()
                    case 32:
                        self.atendente_controller.cadastrarAtendente()
                    case 33:
                        self.medico_controller.buscarMedico()
                    case 34:
                        self.atendente_controller.buscarAtendente()
                    case 35:
                        self.medico_controller.modificarMedico()
                    case 36:
                        self.atendente_controller.modificarAtendente()
                    case 37:
                        self.medico_controller.deletarMedico()
                    case 38:
                        self.atendente_controller.deletarAtendente()
                    case 41:
                        self.banco_dados_controller.mostrar_consultas()
                    case 42:
                        self.banco_dados_controller.valorTotalConsultas()
                    case 43:
                        self.banco_dados_controller.mostrarAtendentes()
                    case 44:
                        self.banco_dados_controller.mostrarClientes()
                    case 45:
                        self.banco_dados_controller.mostrarMedicos()
                    case 46:
                        self.medico_controller.atualizarEndereco()
                    case 47:
                        self.atendente_controller.atualizarEndereco()
                    case 48:
                        self.medico_controller.gerar_receita()
                    case 49:
                        self.medico_controller.gerar_atestado()
                    case 00:
                        break
            except ValueError:
                print("Opção inválida")
                input("Pressione Enter para continuar")
                self.menuView()



                    
if __name__ == "__main__":
    
    menuview = MenuView()
    menuview.menuView()