from .pessoa import Pessoa
import re

class Cliente(Pessoa):
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf, endereco)
        self.__consultas = []

        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido.")

    def validar_cpf(self, cpf):
        return re.match(r'^\d{11}$', cpf) is not None

    @property
    def consultas(self):
        return self.__consultas

    def adicionar_consulta(self, consulta):
        self.__consultas.append(consulta)

    def exibir_detalhes(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"
