from .funcionario import Funcionario

class Atendente(Funcionario):
    def exibir_detalhes(self):
        return f"Atendente: {self.nome}, Login: {self.login}"
