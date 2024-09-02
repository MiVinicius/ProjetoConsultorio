class ControllerCliente:
    def __init__(self, banco_de_dados, view_cliente):
        self.banco_de_dados = banco_de_dados
        self.view_cliente = view_cliente

    def cadastrar_cliente(self, cliente):
        self.banco_de_dados.clientes.append(cliente)
        self.view_cliente.mostrar_cliente(cliente)

    def editar_cliente(self, cliente, novos_dados):
        for key, value in novos_dados.items():
            if hasattr(cliente, key):
                setattr(cliente, key, value)
            else:
                print(f"Atributo {key} não encontrado no cliente.")

    def remover_cliente(self, cliente):
        self.banco_de_dados.clientes.remove(cliente)
        print(f"Cliente {cliente.nome} removido com sucesso.")

    def consultar_cliente(self, cpf):
        for cliente in self.banco_de_dados.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
