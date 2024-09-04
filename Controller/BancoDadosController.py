import sys
sys.path.append('.')
from ProjetoConsultorio.Model.BancoDadosModel import BancoDadosModel
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente


class BancoDadosController:
    
    def __init__(self):
        self.model = BancoDadosModel()

    # Create
    def cadastrarUsuario(self, login, senha, tipo):
        return self.model.cadastrarUsuario(Usuario(login, senha, tipo))
        
    def cadastrarCliente(self, nome, cpf, telefone, endereco):
        return self.model.cadastrarCliente(Cliente(nome, cpf, telefone, endereco))
    
    def cadastrarConsulta(self, descricao, data, horario, valor, cliente, medico):
        return self.model.cadastrarConsulta(Consulta(descricao, data, horario, valor, cliente, medico))
    
    def cadastrarAtendente(self, nome, cpf, telefone, endereco, salario):
        return self.model.cadastrarAtendente(Atendente(nome, cpf, telefone, endereco, salario))
    
    def cadastrarMedico(self, nome, cpf, telefone, endereco, salario, crm):
        return self.model.cadastrarMedico(Medico(nome, cpf, telefone, endereco, salario, crm))
    
    # Retreave
    def buscarUsuario(self, login, senha, tipo):
        return self.model.buscarUsuario(Usuario(login, senha, tipo, False))
        
    def buscarCliente(self, nome, cpf):
        return self.model.buscarCliente(Cliente(nome, cpf, None, None))
    
    def buscarConsulta(self, numero):
        return self.model.buscarConsulta(numero)
    
    def buscarAtendente(self, nome, cpf):
        return self.model.buscarAtendente(Atendente(nome, cpf, None, None, None))
    
    def buscarMedico(self, nome, cpf):
        return self.model.buscarMedico(Medico(nome, cpf, None, None, None, None))
    
    # Update
    def modificarUsuario(self, usuario, login, senha, tipo):
        return self.model.modificarUsuario(usuario, Usuario(login, senha, tipo))
    
    def modificarCliente(self, clienteAntigo, nome, cpf, telefone, endereco):
        return self.model.modificarCliente(clienteAntigo, Cliente(nome, cpf, telefone, endereco))
    
    def modificarConsulta(self, descricao, data, horario, valor, medico, consultaModificar):
        return self.model.modificarConsulta(Consulta(descricao, data, horario, valor, cliente=None, medico=medico), consultaModificar)
    
    def modificarAtendente(self, atendente_existe, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo):
        return self.model.modificarAtendente(atendente_existe, Atendente(nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo))
    
    def modificarMedico(self, medicoAntigo, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo, crmNovo):
        return self.model.modificarMedico(medicoAntigo, Medico(nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo, crmNovo))
    
    # Delete
    def deletarUsuario(self, login):
        return self.model.deletarUsuario(login)
    
    def deletarCliente(self, cliente):
        return self.model.deletarCliente(cliente)
    
    def deletarAtendente(self, atendente):
        return self.model.deletarAtendente(atendente)
    
    def deletarMedico(self, medico):
        return self.model.deletarMedico(medico)
    
    def deletarConsulta(self, consulta):
        return self.model.deletarConsulta(consulta)
    
    # opcionais
    def mostrar_consultas(self):
        return self.model.mostrarConsultas()
    
    def valorTotalConsultas(self):
        return self.model.valorTotalConsultas()
    
    def mostrarAtendentes(self):
        return self.model.mostrarAtendentes()
    
    def mostrarClientes(self):
        return self.model.mostrarClientes()
    
    def mostrarMedicos(self):
        return self.model.mostrarMedicos()

    
