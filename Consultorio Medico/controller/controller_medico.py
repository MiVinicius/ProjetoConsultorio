class ControllerMedico:
    def __init__(self, banco_de_dados, view_menu_medico):
        self.banco_de_dados = banco_de_dados
        self.view_menu_medico = view_menu_medico

    def gerar_receita_medica(self, consulta, texto_receita):
        consulta.gerar_receita(texto_receita)
        print("Receita médica gerada com sucesso.")

    def gerar_atestado_medico(self, consulta, texto_atestado):
        consulta.gerar_atestado(texto_atestado)
        print("Atestado médico gerado com sucesso.")
