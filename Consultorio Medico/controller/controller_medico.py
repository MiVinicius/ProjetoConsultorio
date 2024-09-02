from model.medico import Medico

class ControllerMedico:
    def __init__(self, banco_de_dados, view_medico):
        self.banco_de_dados = banco_de_dados
        self.view_medico = view_medico

    def adicionar_medico(self, nome, cpf, endereco, login, senha, salario, especialidade, crm):
        try:
            medico = Medico(nome, cpf, endereco, login, senha, salario, especialidade, crm)
            self.banco_de_dados.adicionar_medico(medico)
            print("Médico cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar médico: {e}")

    def mostrar_medico(self, crm):
        medico = self.banco_de_dados.buscar_medico(crm)
        if medico:
            self.view_medico.mostrar_medico(medico)
        else:
            print("Médico não encontrado!")

    def remover_medico(self, crm):
        if self.banco_de_dados.remover_medico(crm):
            print("Médico removido com sucesso!")
        else:
            print("Médico não encontrado!")
