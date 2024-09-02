from model_funcionario import ModelFuncionario

class ModelAtendente(ModelFuncionario):
    def __init__(self, nome, cpf, endereco, telefone, login, senha, salario):
        super().__init__(nome, cpf, endereco, telefone, login, senha, salario, "Atendente")

    def mostrar_informacoes(self):
        print(f"Atendente: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}")
