import sys
sys.path.append('.')
from Controller.BancoDadosController import BancoDadosController



class UsuarioController:
    
    def __init__(self, banco_dados_controller):
        self.banco_dados_controller = banco_dados_controller
    
    def cadastrarUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        tipo = int(input("Digite o tipo do usuario: ->Funcionario = 1, Medico = 2<- \n"))
        if BancoDadosController.buscarUsuario(nome, senha, tipo) is None:
            BancoDadosController.cadastrarUsuario(nome, senha, tipo)
            print("o usuario foi Cadastrado")
            input("pressione ENTER para continuar")
            return True
        else:
            print("o usuario não foi Cadastrado")
            input("pressione ENTER para continuar")
            return False
            
    
    def buscarUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        tipo = int(input("Digite o tipo do usuario: ->Funcionario = 1, Medico = 2<- \n"))
        usuario_buscar = BancoDadosController.buscarUsuario(nome, senha, tipo)
        if usuario_buscar is None:
            print("o usuario não existe")
            input("pressione ENTER para continuar")
        else:
            print(usuario_buscar.__str__())
            input("pressione ENTER para continuar")
            return usuario_buscar
            
            
    
    def modificarUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        tipo = int(input("Digite o tipo do usuario: ->Funcionario = 1, Medico = 2<- \n"))
        usuario_existente = BancoDadosController.buscarUsuario(nome, senha, tipo)
        if usuario_existente is None:
            print("o usuario não existe")
            input("pressione ENTER para continuar")
        else:
            nomeNovo = str(input("Digite o novo nome do usuario: \n"))
            senhaNova = str(input("Digite a nova senha do usuario: \n"))
            tipoNovo = int(input("Digite o novo tipo do usuario: ->Funcionario = 1, Medico = 2<- \n"))
            return BancoDadosController.modificarUsuario(usuario_existente, nomeNovo, senhaNova, tipoNovo)
    
    
    def excluirUsuario():
        nome = str(input("Digite o nome do usuario: \n"))
        senha = str(input("Digite a senha do usuario: \n"))
        tipo = int(input("Digite o tipo do usuario: ->Funcionario = 1, Medico = 2<- \n"))
        usuario_existente = BancoDadosController.buscarUsuario(nome, senha, tipo)
        if usuario_existente is None:
            print("o usuario não existe")
            input("pressione ENTER para continuar")
        else:
            try:
                BancoDadosController.deletarUsuario(usuario_existente)
                print("o usuario foi excluído")
                input("pressione ENTER para continuar")
                return True
            except Exception as e:
                print("o usuario não foi excluído, erro", e)
                input("pressione ENTER para continuar")
                return False
            
            
# if __name__ == "__main__":
#     UsuarioController.cadastrarUsuario()
#     UsuarioController.buscarUsuario()
#     UsuarioController.modificarUsuario()
#     UsuarioController.excluirUsuario()