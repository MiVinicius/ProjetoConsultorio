import sys
sys.path.append('.')
class Usuario():
    
    def __init__(self, login, senha, admin = False):
        self.__login = login
        self.__senha = senha
        self.__admin = admin

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha