import sys
sys.path.append('.')
from ProjetoConsultorio.Model.BancoDadosModel import BancoDadosModel
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente


class BancoDadosController():
    
    @staticmethod
    def inicializarBase():
        return BancoDadosModel._inicializarBase()
        
        
    # Create
    @staticmethod
    def cadastrarUsuario(login, senha, tipo):
        return BancoDadosModel.cadastrarUsuario(Usuario(login, senha, tipo))
        
    @staticmethod
    def cadastrarCliente(nome, cpf, telefone, endereco):
        return BancoDadosModel.cadastrarCliente(Cliente(nome, cpf, telefone, endereco))
    
    @staticmethod
    def cadastrarConsulta(descricao, data, horario, valor, cliente):
        return BancoDadosModel.cadastrarConsulta(Consulta(descricao, data, horario, valor, cliente))
    
    @staticmethod
    def cadastrarAtendente(nome, cpf):
        return BancoDadosModel.cadastrarAtendente(Atendente(nome, cpf))
    
    @staticmethod
    def cadastrarMedico(nome, cpf, telefone, endereco, salario, crm):
        return BancoDadosModel.cadastrarMedico(Medico(nome, cpf, telefone, endereco, salario, crm))
    
    
    # Retreave
    
    
    @staticmethod
    def buscarUsuario(login, senha, tipo):
        return BancoDadosModel.buscarUsuario(Usuario(login, senha, tipo))
        
    @staticmethod
    def buscarCliente(nome, cpf):
        return BancoDadosModel.buscarCliente(Cliente(nome, cpf, None, None))
    
    @staticmethod
    def buscarConsulta(numero):
        return BancoDadosModel.buscarConsulta(numero)
    @staticmethod
    def buscarAtendente(nome, cpf):
        return BancoDadosModel.buscarAtendente(Atendente(nome, cpf, None, None, None))
    
    @staticmethod
    def buscarMedico(nome, cpf):
        return BancoDadosModel.buscarMedico(Medico(nome, cpf, None, None, None, None))
    
    
    # Update
    
    @staticmethod
    def modificarUsuario(usuario, login, senha, tipo):
        return BancoDadosModel.modificarUsuario(usuario, Usuario(login, senha, tipo))
    
    @staticmethod
    def modificarCliente(clienteAntigo, nome, cpf, telefone, endereco):
        return BancoDadosModel.modificarCliente(clienteAntigo, Cliente(nome, cpf, telefone, endereco))
    
    @staticmethod
    def modificarConsulta(descricao, data, horario, valor, consultaModificar):
        return BancoDadosModel.modificarConsulta(Consulta(descricao, data, horario, valor, cliente = None), consultaModificar)
    
    @staticmethod
    def modificarAtendente(atendente_existe, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo):
        return BancoDadosModel.modificarAtendente(atendente_existe, Atendente(nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo))
    
    @staticmethod
    def modificarMedico(medicoAntigo, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo, crmNovo):
        return BancoDadosModel.modificarMedico(medicoAntigo, Medico(nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, salarioNovo, crmNovo))
    
    
    # Delete
    
    @staticmethod
    def deletarUsuario(login):
        return BancoDadosModel.deletarUsuario(login)
    
    @staticmethod
    def deletarCliente(cliente):
        return BancoDadosModel.deletarCliente(cliente)
    
    @staticmethod
    def deletarAtendente(atendente):
        return BancoDadosModel.deletarAtendente(atendente)
    
    @staticmethod
    def deletarMedico(medico):
        return BancoDadosModel.deletarMedico(medico)
    
    @staticmethod
    def deletarConsulta(consulta):
        return BancoDadosModel.deletarConsulta(consulta)
    
    # opcionais
    
    @staticmethod
    def mostrar_consultas():
        return BancoDadosModel.mostrarConsultas()
    
    @staticmethod
    def valorTotalConsultas():
        return BancoDadosModel.valorTotalConsultas()
    
    @staticmethod
    def mostrarAtendentes():
        return BancoDadosModel.mostrarAtendentes()
    
    @staticmethod
    def mostrarClientes():
        return BancoDadosModel.mostrarClientes()
    
    @staticmethod
    def mostrarMedicos():
        return BancoDadosModel.mostrarMedicos()
    
