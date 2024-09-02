from model.consulta import Consulta

class ControllerConsulta:
    def __init__(self, banco_de_dados, view_consulta):
        self.banco_de_dados = banco_de_dados
        self.view_consulta = view_consulta

    def adicionar_consulta(self, descricao, data, horario, valor, cliente, medico):
        consulta = Consulta(descricao, data, horario, valor, cliente, medico)
        self.banco_de_dados.adicionar_consulta(consulta)
        cliente.adicionar_consulta(consulta)
        print("Consulta agendada com sucesso!")

    def mostrar_consulta(self, cliente_cpf):
        cliente = self.banco_de_dados.buscar_cliente(cliente_cpf)
        if cliente:
            consultas = cliente.consultas
            if consultas:
                for consulta in consultas:
                    self.view_consulta.mostrar_consulta(consulta)
            else:
                print("Nenhuma consulta encontrada para este cliente.")
        else:
            print("Cliente não encontrado!")

    def remover_consulta(self, cliente_cpf):
        if self.banco_de_dados.remover_consulta(cliente_cpf):
            print("Consulta removida com sucesso!")
        else:
            print("Consulta não encontrada!")
