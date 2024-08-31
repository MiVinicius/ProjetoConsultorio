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
            return True
        else:
            print("o usuario não foi Cadastrado")
            input("pressione ENTER para continuar")
            return False
            
    @staticmethod
    def buscarUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        if BancoDadosController.buscarUsuario(nome, senha) is None:
            print("o usuario não existe")
            input("pressione ENTER para continuar")
        else:
            print(BancoDadosController.buscarUsuario(nome, senha).__str__())
            input("pressione ENTER para continuar")
            
    @staticmethod
    def modificarUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        usuario_existente = BancoDadosController.buscarUsuario(nome, senha)
        if usuario_existente is None:
            print("o usuario não existe")
            input("pressione ENTER para continuar")
        else:
            nomeNovo = str(input("Digite o novo nome do usuario: \n"))
            senhaNova = str(input("Digite a nova senha do usuario: \n"))
            return BancoDadosController.modificarUsuario(usuario_existente, nomeNovo, senhaNova)
    
    @staticmethod
    def excluirUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        usuario_existente = BancoDadosController.buscarUsuario(nome, senha)
        if usuario_existente is None:
            print("o usuario não existe")
            input("pressione ENTER para continuar")
        else:
            return BancoDadosController.deletarUsuario(usuario_existente)
            
            
    