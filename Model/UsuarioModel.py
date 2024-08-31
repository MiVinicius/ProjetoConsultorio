import sys
sys.path.append('.')
class Usuario():
    
    def __init__(self, login: str, senha: str, tipo: int, admin: bool = False):
        self.__login = login
        self.__senha = senha
        self.__tipo = tipo
        self.__admin = admin

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def admin(self):
        return self.__admin