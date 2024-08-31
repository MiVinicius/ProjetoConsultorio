import sys
sys.path.append('.')
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
from ProjetoConsultorio.Controller.ClienteController import ClienteController
from ProjetoConsultorio.Controller.ConsultaController import ConsultaController
from ProjetoConsultorio.Controller.MedicoController import MedicoController
from ProjetoConsultorio.Controller.FuncionarioController import FuncionarioController
import os

def clear():
    return os.system('cls')

class MenuView():
    
    def menuView(self):
        
        while True:
            print("""
                ------------------------------------------------
                |Menu 1x    Menu 2x      Menu 3x       Menu 4x | 
                |Cliente   Consulta    Funcionários  financeiro|
                ------------------------------------------------  

11 - Cadastrar Cliente			21 - Agendamento de consulta
12 - Buscar Cliente			22 - Verificar histórico de consultas
13 - Modificar dados do cliente		23 - Modificar consulta
14 - Remover cliente 			24 - Cancelar consulta

31 - Cadastrar Médico			41 - Todas as Consultas agendadas
32 - Cadastrar Funcionário		42 - valor total das consultas agendadas
33 - Buscar Médico			43 - Mostrar todos os funcionários
34 - Buscar Funcionário                 44 - Mostrar todos os clientes
35 - Modificar dados de Médico          00 - Sair
36 - Modificar dados de Funcionário
37 - Remover Médico
38 - Remover Funcionário

                """)
            opcao = int(input("Digite o número correspondente ao menu: "))
            match opcao:
                case 11:
                    ClienteController.cadastrarCliente()
                case 12:
                    ClienteController.buscarCliente()
                case 13:
                    ClienteController.modificarCliente()
                case 14:
                    ClienteController.deletarCliente()
                case 21:
                    ConsultaController.cadastrarConsulta()
                case 22:
                    ConsultaController.buscarConsulta()
                case 23:
                    ConsultaController.modificarConsulta()
                case 24:
                    ConsultaController.deletarConsulta2()
                case 31:
                    MedicoController.cadastrarMedico()
                case 32:
                    FuncionarioController.cadastrarFuncionario()
                case 33:
                    MedicoController.buscarMedico()
                case 34:
                    FuncionarioController.buscarFuncionario()
                case 35:
                    MedicoController.modificarMedico()
                case 36:
                    FuncionarioController.modificarFuncionario()
                case 37:
                    MedicoController.deletarMedico()
                case 38:
                    FuncionarioController.deletarFuncionario()
                case 41:
                    BancoDadosController.mostrar_consultas()
                case 42:
                    BancoDadosController.valorTotalConsultas()
                case 43:
                    BancoDadosController.mostrarFuncionarios()
                case 44:
                    BancoDadosController.mostrarClientes()
                case 00:
                    break
                case _:
                    clear()
                    print("Opção invalida")
                    input("Pressione Enter para continuar")
                    
if __name__ == "__main__":
    
    menuview = MenuView()
    menuview.menuView()