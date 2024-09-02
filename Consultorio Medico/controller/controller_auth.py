class ControllerAuth:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def autenticar_funcionario(self, login, senha):
        funcionario = self.banco_de_dados.buscar_atendente(login) or self.banco_de_dados.buscar_medico(login)
        if funcionario and funcionario.autenticar(login, senha):
            return funcionario
        print("Autenticação falhou.")
        return None
