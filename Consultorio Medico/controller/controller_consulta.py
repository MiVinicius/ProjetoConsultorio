class ControllerConsulta:
    def __init__(self, banco_de_dados, view_consulta):
        self.banco_de_dados = banco_de_dados
        self.view_consulta = view_consulta

    def cadastrar_consulta(self, consulta):
        self.banco_de_dados.consultas.append(consulta)
        self.view_consulta.mostrar_consulta(consulta)

    def editar_consulta(self, consulta, novos_dados):
        for key, value in novos_dados.items():
            if hasattr(consulta, key):
                setattr(consulta, key, value)
            else:
                print(f"Atributo {key} não encontrado na consulta.")

    def remover_consulta(self, consulta):
        self.banco_de_dados.consultas.remove(consulta)
        print(f"Consulta {consulta.descricao} removida com sucesso.")

    def consultar_consulta(self, descricao):
        for consulta in self.banco_de_dados.consultas:
            if consulta.descricao == descricao:
                return consulta
        return None
