from .funcionario import Funcionario
import re

class Medico(Funcionario):
    def __init__(self, nome, cpf, endereco, login, senha, salario, especialidade, crm):
        super().__init__(nome, cpf, endereco, login, senha, salario)
        self.__especialidade = especialidade
        self.__crm = crm

        if not self.validar_crm(crm):
            raise ValueError("CRM inválido.")

    def validar_crm(self, crm):
        return re.match(r'^\d{4,6}$', crm) is not None

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def crm(self):
        return self.__crm

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    @crm.setter
    def crm(self, crm):
        self.__crm = crm

    def exibir_detalhes(self):
        return f"Médico: {self.nome}, CRM: {self.crm}, Especialidade: {self.especialidade}"
