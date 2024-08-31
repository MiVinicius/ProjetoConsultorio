# from Model.BancoDadosModel import BancoDadosModel
from View.LoginView import LoginView
# from View.MenuView import MenuView
from Controller.BancoDadosController import BancoDadosController
# from ProjetoConsultorio.View.Login import realizar_login

def Main():
    
    BancoDadosController().inicializarBase()  
    
    # MenuView().menuView()
    LoginView()
    # realizar_login()
    
    

if __name__ == "__main__":
    Main()