from model_pessoa import ModelPessoa

class ModelCliente(ModelPessoa):
    def __init__(self, nome, cpf, endereco, telefone, consultas=None):
        super().__init__(nome, cpf, endereco, telefone)
        self.consultas = consultas or []

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def mostrar_informacoes(self):
        print(f"Cliente: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco.rua}, {self.endereco.numero}, {self.endereco.bairro}, {self.endereco.cidade}, {self.endereco.cep}")
        print("Consultas:")
        for consulta in self.consultas:
            print(consulta.descricao)
