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
        self.menu()

    def menu(self):
        while True:
            # clear()
            print("-----------" * 6)
            print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
            print("-----------" * 6)
            print("Deseja logar ou cadastrar?")
            print("-----------" * 6)
            print("1 - Logar  --  2 - Cadastrar")
            print()
            opcao = str(input("Opção: "))
            print("-----------" * 6)
            try:
                if opcao == "1":
                    self.login()
                    break
                elif opcao == "2":
                    self.cadastro()
                    break
                else:
                    print('Opção inválida')
                    input("Pressione ENTER para continuar")
            except Exception as e:
                print("Ocorreu um erro", e, "! Tente novamente")
                input("Pressione ENTER para continuar")
                self.menu()
    
    def login(self):
        # clear()
        print("-----------"*6)
        print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
        print("-----------"*6)
        print("Login necessário")
        print("-----------"*6)
        login = input(str("Login: "))
        senha = input(str("Senha: "))
        print("->Atendente = 1, Medico = 2<-")
        tipo = input(str("Tipo: "))
        print("-----------"*6)
        try:
            verificar = BancoDadosController.buscarUsuario(login, senha, int(tipo))
            if verificar is not None:
                if verificar.admin is True:
                    MenuView().menuView()
                elif verificar.tipo == 1:
                    MenuViewAtendente().menuView()
                elif verificar.tipo == 2:
                    MenuViewMedico().menuView()
                else:
                    print("Esse sistema não é pra você!")
                    input("pressione ENTER para continuar")
                    self.menu()
            else:
                print('login ou senha incorreta')
                input("pressione ENTER para continuar")
                self.login()
        except Exception as e:
            print('Ocorreu um erro', e)
            self.login()
            
    def cadastro(self):
        # clear()
        print("-----------"*6)
        print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
        print("-----------"*6)
        print("Cadastre-se")
        print("-----------"*6)
        login = input(str("Login: "))
        senha = input(str("Senha: "))
        print("->Funcionario = 1, Medico = 2<-")
        tipo = int(input(str("Tipo: ")))
        print("-----------"*6)
        try:
            verificar = BancoDadosController.buscarUsuario(login, senha, tipo)
            if verificar is None:
                BancoDadosController.cadastrarUsuario(login, senha, tipo)
                print("Cadastrado com sucesso")
                input("pressione ENTER para continuar")
                self.menu()
            else:
                print('login ou senha incorreta')
                input("pressione ENTER para continuar")
                self.menu()
        except Exception as e:
            print('Ocorreu um erro', e)
            self.cadastro()
            
    
# if __name__ == "__main__":            
#     loginview = LoginView()