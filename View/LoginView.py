import sys
sys.path.append('.')
from ProjetoConsultorio.View.MenuView import MenuView
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController
import os

def clear():
    return os.system('cls')

class LoginView:
    
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            clear()
            print("-----------" * 6)
            print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
            print("-----------" * 6)
            print("Deseja logar ou cadastrar?")
            print("-----------" * 6)
            print("1 - Logar  --  2 - Cadastrar")
            print()
            opcao = input("Opção: ")
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
        clear()
        print("-----------"*6)
        print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
        print("-----------"*6)
        print("Login necessário")
        print("-----------"*6)
        login = input(str("Login: "))
        senha = input(str("Senha: "))
        print("->Funcionario = 1, Medico = 2<-")
        tipo = int(input(str("Tipo: ")))
        print("-----------"*6)
        try:
            verificar = BancoDadosController.buscarUsuario(login, senha, tipo)
            if verificar is not None:
                
                if verificar.admin is True:
                    MenuView().menuView()
                elif verificar.tipo == 1:
                    MenuView().menuView()
                elif verificar.tipo == 2:
                    MenuView().menuView()
                else:
                    print("Esse sistema não é pra você!")
                    input("pressione ENTER para continuar")
                    self.menu()
            else:
                
                print('login ou senha incorreta')
        except Exception as e:
            
            print('Ocorreu um erro', e)
            self.login()
            
    def cadastro(self):
        clear()
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