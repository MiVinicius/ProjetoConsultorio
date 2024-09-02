class ControllerAdministrador:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def criar_administrador(self, nome, cpf, endereco, telefone, login, senha, salario):
        administrador_atual = self.obter_administrador_logado()
        administrador_atual.criar_administrador(self.banco_de_dados, nome, cpf, endereco, telefone, login, senha, salario)

    def editar_administrador(self, administrador, novos_dados):
        administrador_atual = self.obter_administrador_logado()
        administrador_atual.editar_administrador(administrador, **novos_dados)

    def remover_administrador(self, administrador):
        administrador_atual = self.obter_administrador_logado()
        administrador_atual.remover_administrador(self.banco_de_dados, administrador)

    def obter_administrador_logado(self):
        # Supondo que o administrador logado é obtido de alguma forma, 
        # como de uma sessão ou diretamente do banco de dados.
        # Aqui, retornamos o primeiro administrador como exemplo.
        return self.banco_de_dados.administradores[0]  # Ou outro método de obter o administrador logado
