import sys
sys.path.append('.')
class Usuario:
    def __init__(self, login: str, senha: str, tipo: int, admin: bool = False, id: int = None):
        self.login = login
        self.senha = senha
        self.tipo = tipo
        self.admin = admin
        self.__id = id  

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        if not isinstance(login, str) or not login.strip():
            raise ValueError("O login deve ser uma string não vazia.")
        self.__login = login.strip()

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        if not isinstance(senha, str) or len(senha) < 5:
            raise ValueError("A senha deve ter pelo menos 5 caracteres.")
        self.__senha = senha

    @property
    def tipo(self) -> int:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: int):
        if not isinstance(tipo, int) or tipo < 0:
            raise ValueError("O tipo deve ser um número inteiro positivo.")
        self.__tipo = tipo

    @property
    def admin(self) -> bool:
        return self.__admin

    @admin.setter
    def admin(self, admin: bool):
        if not isinstance(admin, bool):
            raise ValueError("O valor de admin deve ser booleano.")
        self.__admin = admin

    @property
    def id(self) -> int:
        return self.__id

    def __repr__(self):
        admin_status = "Sim" if self.admin else "Não"
        return (f"Usuário(login={self.__login}, tipo={self.__tipo}, admin={admin_status}")

    