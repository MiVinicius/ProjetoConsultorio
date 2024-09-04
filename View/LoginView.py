import sys
sys.path.append('.')
from ProjetoConsultorio.View.MenuView import MenuView
from ProjetoConsultorio.View.MenuViewMedico import MenuViewMedico
from ProjetoConsultorio.View.MenuViewAtendente import MenuViewAtendente
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
import os


def clear():
    return os.system('cls')

class LoginView:

    def __init__(self):
        self.BancoDadosController = BancoDadosController()  # isso nem deveria estar aqui...
        self.menu()

    def menu(self):
        while True:
            print("-----------" * 6)
            print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
            print("-----------" * 6)
            print("Deseja logar ou cadastrar?")
            print("-----------" * 6)
            print("1 - Logar  --  2 - Cadastrar")
            print()
            opcao = input("Opção: ").strip()
            print("-----------" * 6)
            if opcao == "1":
                self.login()
                break
            elif opcao == "2":
                self.cadastro()
                break
            else:
                print('Opção inválida')
                input("Pressione ENTER para continuar")

    def login(self):
        while True:
            print("-----------" * 6)
            print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
            print("-----------" * 6)
            print("Login necessário")
            print("-----------" * 6)
            login = input("Login: ").strip()
            senha = input("Senha: ").strip()
            print("->Atendente = 1, Medico = 2<-")
            tipo = input("Tipo: ").strip()
            print("-----------" * 6)

            if not login or not senha or not tipo.isdigit():
                print("Dados inválidos. Tente novamente.")
                input("Pressione ENTER para continuar")
                continue

            tipo = int(tipo)
            try:
                usuario = self.BancoDadosController.buscarUsuario(login, senha, tipo)
                if usuario:
                    if usuario.admin:
                        MenuView(self.BancoDadosController).menuView()
                    elif usuario.tipo == 1:
                        MenuViewAtendente(self.BancoDadosController).menuView()
                    elif usuario.tipo == 2:
                        MenuViewMedico(self.BancoDadosController).menuView()
                    else:
                        print("Esse sistema não é para você!")
                        input("Pressione ENTER para continuar")
                        self.menu()
                    break
                else:
                    print('Login ou senha incorretos')
                    input("Pressione ENTER para continuar")
            except Exception as e:
                print('Ocorreu um erro:', e)
                input("Pressione ENTER para continuar")

    def cadastro(self):
        while True:
            print("-----------" * 6)
            print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
            print("-----------" * 6)
            print("Cadastre-se")
            print("-----------" * 6)
            login = input("Login: ").strip()
            senha = input("Senha: ").strip()
            print("->Atendente = 1, Medico = 2<-")
            tipo = input("Tipo: ").strip()
            print("-----------" * 6)

            if not login or not senha or not tipo.isdigit():
                print("Dados inválidos. Tente novamente.")
                input("Pressione ENTER para continuar")
                continue

            tipo = int(tipo)
            try:
                usuario_existente = self.BancoDadosController.buscarUsuario(login, senha, tipo)
                if usuario_existente is None:
                    self.BancoDadosController.cadastrarUsuario(login, senha, tipo)
                    print("Cadastrado com sucesso")
                    input("Pressione ENTER para continuar")
                    self.menu()
                    break
                else:
                    print('Login já existe. Tente outro.')
                    input("Pressione ENTER para continuar")
            except Exception as e:
                print('Ocorreu um erro:', e)
                input("Pressione ENTER para continuar")


            
    
# if __name__ == "__main__":            
#     loginview = LoginView()