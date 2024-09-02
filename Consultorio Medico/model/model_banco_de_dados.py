import os
import json
from model_cliente import ModelCliente
from model_consulta import ModelConsulta
from model_medico import ModelMedico
from model_atendente import ModelAtendente
from model_administrador import ModelAdministrador

class ModelBancoDeDados:
    def __init__(self):
        self.clientes = []
        self.consultas = []
        self.medicos = []
        self.atendentes = []
        self.administradores = []
        self.diretorio_dados = 'data'

        if not os.path.exists(self.diretorio_dados):
            os.makedirs(self.diretorio_dados)

    def salvar_dados(self):
        data = {
            'clientes': [c.__dict__ for c in self.clientes],
            'consultas': [c.__dict__ for c in self.consultas],
            'medicos': [m.__dict__ for m in self.medicos],
            'atendentes': [a.__dict__ for a in self.atendentes],
            'administradores': [adm.__dict__ for adm in self.administradores],
        }
        caminho_arquivo = os.path.join(self.diretorio_dados, 'banco_de_dados.json')
        with open(caminho_arquivo, 'w') as file:
            json.dump(data, file, default=str, indent=4)

    def carregar_dados(self):
        caminho_arquivo = os.path.join(self.diretorio_dados, 'banco_de_dados.json')
        try:
            with open(caminho_arquivo, 'r') as file:
                data = json.load(file)
                self.clientes = [ModelCliente(**c) for c in data.get('clientes', [])]
                self.consultas = [ModelConsulta(**c) for c in data.get('consultas', [])]
                self.medicos = [ModelMedico(**m) for m in data.get('medicos', [])]
                self.atendentes = [ModelAtendente(**a) for a in data.get('atendentes', [])]
                self.administradores = [ModelAdministrador(**adm) for adm in data.get('administradores', [])]
        except FileNotFoundError:
            print("Arquivo de dados não encontrado, iniciando com banco de dados vazio.")
