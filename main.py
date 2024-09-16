
import Model.TabelaModel
from Controller.BancoDadosController import BancoDadosController
from View.LoginView import LoginView



def Main():


    Model.TabelaModel.main()
    bancoDados = BancoDadosController()
    LoginView(bancoDados)




if __name__ == "__main__":
    Main()