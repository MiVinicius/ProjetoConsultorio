from model.atendente import Atendente

class ControllerAtendente:
    def __init__(self, banco_de_dados, view_atendente):
        self.banco_de_dados = banco_de_dados
        self.view_atendente = view_atendente

    def adicionar_atendente(self, nome, cpf, endereco, login, senha, salario):
        atendente = Atendente(nome, cpf, endereco, login, senha, salario)
        self.banco_de_dados.adicionar_atendente(atendente)
        print("Atendente cadastrado com sucesso!")

    def mostrar_atendente(self, login):
        atendente = self.banco_de_dados.buscar_atendente(login)
        if atendente:
            self.view_atendente.mostrar_atendente(atendente)
        else:
            print("Atendente não encontrado!")

    def remover_atendente(self, login):
        if self.banco_de_dados.remover_atendente(login):
            print("Atendente removido com sucesso!")
        else:
            print("Atendente não encontrado!")
