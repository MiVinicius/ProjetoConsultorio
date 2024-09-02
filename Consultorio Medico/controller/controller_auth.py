class ControllerAuth:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def autenticar_usuario(self):
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        for administrador in self.banco_de_dados.administradores:
            if administrador.login == login and administrador.verificar_senha(senha):
                print(f"Bem-vindo, Administrador {administrador.nome}!")
                return administrador

        for medico in self.banco_de_dados.medicos:
            if medico.login == login and medico.verificar_senha(senha):
                print(f"Bem-vindo, Dr(a). {medico.nome}!")
                return medico

        for atendente in self.banco_de_dados.atendentes:
            if atendente.login == login and atendente.verificar_senha(senha):
                print(f"Bem-vindo, Atendente {atendente.nome}!")
                return atendente

        print("Login ou senha incorretos. Tente novamente.")
        return None
