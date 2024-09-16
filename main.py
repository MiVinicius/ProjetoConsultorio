
from View.LoginView import LoginView

import Model.TabelaModel
from ProjetoConsultorio.Controller.BancoDadosController import BancoDadosController



def Main():


    Model.TabelaModel.main()
    bancoDados = BancoDadosController()
    LoginView(bancoDados)




if __name__ == "__main__":
    Main()