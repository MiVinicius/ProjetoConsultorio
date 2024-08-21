import sys
sys.path.append('.')
from ProjetoConsultorio.Model.BancoDadosModel import BancoDadosModel
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.ConsultaModel import Consulta


class BancoDadosController():
    
    @staticmethod
    def inicializarBase():
        BancoDadosModel._inicializarBase()
        
    @staticmethod
    def cadastrar_usuario(login, senha):
        return BancoDadosModel.cadastrarUsuario(Usuario(login, senha))
        
    @staticmethod
    def cadastrarCliente(nome, cpf):
        return BancoDadosModel.cadastrarCliente(Cliente(nome, cpf))
    
    @staticmethod
    def cadastrarConsulta(descricao, data):
        return BancoDadosModel.cadastrarConsulta(Consulta(descricao, data))
    
    @staticmethod
    def buscarUsuario(login, senha):
        return BancoDadosModel.buscarUsuario(login, senha)
        
    @staticmethod
    def buscarCliente(nome, cpf):
        return BancoDadosModel.buscarCliente(Cliente(nome, cpf))
    
    @staticmethod
    def buscarConsulta(consulta):
        return BancoDadosModel.buscarConsulta(consulta)
    
    @staticmethod
    def modificarCliente(cliente):
        return BancoDadosModel.modificarCliente(cliente)
    
    @staticmethod
    def modificarConsulta(consulta, consulta_nova):
        return BancoDadosModel.modificarConsulta(consulta, consulta_nova)
    
    @staticmethod
    def deletarCliente(cliente):
        return BancoDadosModel.deletarCliente(cliente)
    
    @staticmethod
    def cadastrarFuncionario(funcionario):
        return BancoDadosModel.cadastrarFuncionario(funcionario)
    
    @staticmethod
    def buscarFuncionario(funcionario):
        return BancoDadosModel.buscarFuncionario(funcionario)
    
    @staticmethod
    def modificarFuncionario(funcionario):
        return BancoDadosModel.modificarFuncionario(funcionario)
    
    @staticmethod
    def deletarFuncionario(funcionario):
        return BancoDadosModel.deletarFuncionario(funcionario)
    
    @staticmethod
    def cadastrarMedico(medico):
        return BancoDadosModel.cadastrarMedico(medico)
    
    @staticmethod
    def buscarMedico(medico):
        return BancoDadosModel.buscarMedico(medico)
    
    @staticmethod
    def modificarMedico(medico):
        return BancoDadosModel.modificarMedico(medico)
    
    @staticmethod
    def deletarMedico(medico):
        return BancoDadosModel.deletarMedico(medico)
    
    @staticmethod
    def mostrar_consultas():
        return BancoDadosModel.mostrarConsultas()