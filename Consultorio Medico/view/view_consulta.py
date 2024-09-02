class ViewConsulta:
    def mostrar_consulta(self, consulta):
        print(f"Consulta: {consulta.descricao}, Data: {consulta.data}, Horário: {consulta.horario}, "
              f"Valor: R$ {consulta.valor:.2f}, Cliente: {consulta.cliente.nome}, Médico: {consulta.medico.nome}")
