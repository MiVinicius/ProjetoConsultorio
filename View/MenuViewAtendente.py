import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController
from ProjetoConsultorio.Controller.ConsultaController import ConsultaController
import os

def clear():
    return os.system('cls')

class MenuViewAtendente():
    
    def menuView(self):
        
        while True:
            #clear()  # OBSERVAÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ISSO FAZ A TELA APAGAR NO TERMINAL SEMPRE QUE VOLTAR PRA LÁ
            print("""
                ----------------------------------------------------
                |Menu 1x    Menu 2x      Menu 3x       Menu 4x     | 
                |Cliente   Consulta    Atendentes  Administrativo|
                ----------------------------------------------------  

11 - Cadastrar Cliente			21 - Agendar consulta
12 - Buscar Cliente			22 - Verificar histórico de consultas do cliente
13 - Modificar dados do cliente		23 - Modificar consulta (precisa do numero da consulta)
14 - Remover cliente 			24 - Cancelar consulta

41 - Todas as Consultas agendadas
42 - valor total do faturamento das consultas agendadas
44 - Mostrar todos os clientes
45 - Mostrar todos os médicos
00 - Sair



                """)
            opcao = int(input("Digite o número correspondente ao menu: "))
            match opcao:
                case 11:
                    ClienteController.cadastrarCliente()  # esses comandos eu deveria colocar na View própria...
                case 12:
                    ClienteController.buscarCliente()
                case 13:
                    ClienteController.modificarCliente()
                case 14:
                    ClienteController.deletarCliente()
                case 21:
                    ConsultaController.cadastrarConsulta()
                case 22:
                    ConsultaController.buscarNumeroListaConsulta()
                case 23:
                    ConsultaController.modificarConsulta()
                case 24:
                    ConsultaController.deletarConsulta()
                case 41:
                    BancoDadosController.mostrar_consultas()
                case 42:
                    BancoDadosController.valorTotalConsultas()
                case 44:
                    BancoDadosController.mostrarClientes()
                case 00:
                    break
                case _:
                    clear()
                    print("Opção invalida")
                    input("Pressione Enter para continuar")
                    
# if __name__ == "__main__":
    
    # menuview = MenuView()
    # menuview.menuView()