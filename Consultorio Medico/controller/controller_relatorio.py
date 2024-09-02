class ControllerRelatorio:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def gerar_relatorio_consultas(self):
        total_consultas, receita_total = self.banco_de_dados.relatorio_consultas()
        print(f"Total de Consultas: {total_consultas}")
        print(f"Receita Total: R$ {receita_total:.2f}")

    def gerar_relatorio_clientes(self):
        total_clientes = self.banco_de_dados.relatorio_clientes()
        print(f"Total de Clientes: {total_clientes}")
