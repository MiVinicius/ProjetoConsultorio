import sys
sys.path.append('.')
from ProjetoConsultorio.View.MenuView import MenuView
import os

def clear():
    return os.system('cls')

class LoginView():
    
    def __init__(self):
        clear()
        print("-----------"*6)
        print("Bem-vindo ao Clinitech, seu Software para clínicas Médicas")
        print("-----------"*6)
        print("Login necessário")
        print("-----------"*6)
        login = input(str("Login: "))
        senha = input(str("Senha: "))
        print("-----------"*6)
        if login =="admin" and senha == "admin":
            clear()
            MenuView().menuView()
        else:
            clear()
            print('login ou senha incorreta')
            LoginView()
            
    
if __name__ == "__main__":            
    loginview = LoginView()
    loginview.loginView()
