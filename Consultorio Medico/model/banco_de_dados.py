import json
from .cliente import Cliente
from .consulta import Consulta
from .medico import Medico
from .atendente import Atendente
from .funcionario import Funcionario

class BancoDeDados:
    def __init__(self):
        self.clientes = []
        self.consultas = []
        self.medicos = []
        self.atendentes = []
        self.funcionarios = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.salvar_dados()

    def remover_cliente(self, cpf):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            self.clientes.remove(cliente)
            self.salvar_dados()
            return True
        return False

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)
        self.salvar_dados()

    def remover_consulta(self, cliente_cpf):
        consulta = next((c for c in self.consultas if c.cliente.cpf == cliente_cpf), None)
        if consulta:
            self.consultas.remove(consulta)
            self.salvar_dados()
            return True
        return False

    def adicionar_medico(self, medico):
        self.medicos.append(medico)
        self.salvar_dados()

    def remover_medico(self, crm):
        medico = self.buscar_medico(crm)
        if medico:
            self.medicos.remove(medico)
            self.salvar_dados()
            return True
        return False

    def adicionar_atendente(self, atendente):
        self.atendentes.append(atendente)
        self.salvar_dados()

    def remover_atendente(self, login):
        atendente = self.buscar_atendente(login)
        if atendente:
            self.atendentes.remove(atendente)
            self.salvar_dados()
            return True
        return False

    def buscar_cliente(self, cpf):
        return next((c for c in self.clientes if c.cpf == cpf), None)

    def buscar_medico(self, crm):
        return next((m for m in self.medicos if m.crm == crm), None)

    def buscar_atendente(self, login):
        return next((a for a in self.atendentes if a.login == login), None)

    def salvar_dados(self):
        data = {
            'clientes': [c.__dict__ for c in self.clientes],
            'consultas': [c.__dict__ for c in self.consultas],
            'medicos': [m.__dict__ for m in self.medicos],
            'atendentes': [a.__dict__ for a in self.atendentes],
        }
        with open('banco_de_dados.json', 'w') as file:
            json.dump(data, file, default=str, indent=4)

    def carregar_dados(self):
        try:
            with open('banco_de_dados.json', 'r') as file:
                data = json.load(file)
                self.clientes = [Cliente(**c) for c in data.get('clientes', [])]
                self.consultas = [Consulta(**c) for c in data.get('consultas', [])]
                self.medicos = [Medico(**m) for m in data.get('medicos', [])]
                self.atendentes = [Atendente(**a) for a in data.get('atendentes', [])]
        except FileNotFoundError:
            pass

    def relatorio_consultas(self):
        total_consultas = len(self.consultas)
        receita_total = sum(consulta.valor for consulta in self.consultas)
        return total_consultas, receita_total

    def relatorio_clientes(self):
        return len(self.clientes)
