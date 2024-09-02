from model.cliente import Cliente

class ControllerCliente:
    def __init__(self, banco_de_dados, view_cliente):
        self.banco_de_dados = banco_de_dados
        self.view_cliente = view_cliente

    def adicionar_cliente(self, nome, cpf, endereco):
        try:
            cliente = Cliente(nome, cpf, endereco)
            self.banco_de_dados.adicionar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar cliente: {e}")

    def mostrar_cliente(self, cpf):
        cliente = self.banco_de_dados.buscar_cliente(cpf)
        if cliente:
            self.view_cliente.mostrar_cliente(cliente)
        else:
            print("Cliente não encontrado!")

    def remover_cliente(self, cpf):
        if self.banco_de_dados.remover_cliente(cpf):
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado!")
