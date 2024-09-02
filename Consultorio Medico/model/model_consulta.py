class ModelConsulta:
    def __init__(self, descricao, data, horario, valor, cliente, medico, receita=None, atestado=None):
        self.descricao = descricao
        self.data = data
        self.horario = horario
        self.valor = valor
        self.cliente = cliente
        self.medico = medico
        self.receita = receita
        self.atestado = atestado

    def gerar_receita(self, texto_receita):
        self.receita = texto_receita

    def gerar_atestado(self, texto_atestado):
        self.atestado = texto_atestado

    def mostrar_informacoes(self):
        print(f"Consulta: {self.descricao}, Data: {self.data}, Horário: {self.horario}, Valor: {self.valor}")
        print(f"Médico: {self.medico.nome}")
        if self.receita:
            print(f"Receita: {self.receita}")
        if self.atestado:
            print(f"Atestado: {self.atestado}")
