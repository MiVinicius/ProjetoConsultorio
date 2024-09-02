from model_funcionario import ModelFuncionario

class ModelMedico(ModelFuncionario):
    def __init__(self, nome, cpf, endereco, telefone, login, senha, salario, crm, especialidade):
        super().__init__(nome, cpf, endereco, telefone, login, senha, salario, "Medico")
        self.crm = crm
        self.especialidade = especialidade

    def mostrar_informacoes(self):
        print(f"Médico: {self.nome}, CRM: {self.crm}, Especialidade: {self.especialidade}")
