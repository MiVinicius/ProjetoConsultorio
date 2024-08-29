import sys
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
sys.path.append('.')


class UsuarioController:
    
    @staticmethod
    def cadastrarUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        if BancoDadosController.buscarUsuario(nome, senha) is None:
            BancoDadosController.cadastrarUsuario(nome, senha)
            print("o usuario foi Cadastrado")
            input("pressione ENTER para continuar")
        else:
            print("o usuario não foi Cadastrado")
            input("pressione ENTER para continuar")
            
    