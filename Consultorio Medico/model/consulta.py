class Consulta:
    def __init__(self, descricao, data, horario, valor, cliente, medico):
        self.__descricao = descricao
        self.__data = data
        self.__horario = horario
        self.__valor = valor
        self.__cliente = cliente
        self.__medico = medico

    @property
    def descricao(self):
        return self.__descricao

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def valor(self):
        return self.__valor

    @property
    def cliente(self):
        return self.__cliente

    @property
    def medico(self):
        return self.__medico

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @data.setter
    def data(self, data):
        self.__data = data

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    def exibir_detalhes(self):
        return (f"Consulta: {self.descricao}, Data: {self.data}, Horário: {self.horario}, "
                f"Valor: R$ {self.valor:.2f}, Cliente: {self.cliente.nome}, Médico: {self.medico.nome}")
