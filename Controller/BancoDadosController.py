import sys
sys.path.append('.')
from ProjetoConsultorio.Model.BancoDadosModel import BancoDadosModel
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario


class BancoDadosController():
    
    @staticmethod
    def inicializarBase():
        BancoDadosModel._inicializarBase()
        
        
    # Create
    @staticmethod
    def cadastrarUsuario(login, senha):
        return BancoDadosModel.cadastrarUsuario(Usuario(login, senha))
        
    @staticmethod
    def cadastrarCliente(nome, cpf):
        return BancoDadosModel.cadastrarCliente(Cliente(nome, cpf))
    
    @staticmethod
    def cadastrarConsulta(descricao, data, cliente):
        return BancoDadosModel.cadastrarConsulta(Consulta(descricao, data, cliente))
    
    @staticmethod
    def cadastrarFuncionario(nome, cpf):
        return BancoDadosModel.cadastrarFuncionario(Funcionario(nome, cpf))
    
    @staticmethod
    def cadastrarMedico(nome, cpf):
        return BancoDadosModel.cadastrarMedico(Medico(nome, cpf))
    
    
    # Retreave
    
    
    @staticmethod
    def buscarUsuario(login, senha):
        return BancoDadosModel.buscarUsuario(Usuario(login, senha))
        
    @staticmethod
    def buscarCliente(nome, cpf):
        return BancoDadosModel.buscarCliente(Cliente(nome, cpf))
    
    @staticmethod
    def buscarConsulta(numero):
        return BancoDadosModel.buscarConsulta(numero)
    @staticmethod
    def buscarFuncionario(nome, cpf):
        return BancoDadosModel.buscarFuncionario(Funcionario(nome, cpf))
    
    @staticmethod
    def buscarMedico(nome, cpf):
        return BancoDadosModel.buscarMedico(Medico(nome, cpf))
    
    
    # Update
    
    @staticmethod
    def modificarCliente(clienteAntigo, nome, cpf):
        return BancoDadosModel.modificarCliente(clienteAntigo, Cliente(nome, cpf))
    
    @staticmethod
    def modificarConsulta(descricao, data, consultaModificar, cliente):
        return BancoDadosModel.modificarConsulta(Consulta(descricao, data, cliente), consultaModificar)
    
    @staticmethod
    def modificarFuncionario(idfuncionario, funcionario_novo):
        return BancoDadosModel.modificarFuncionario(idfuncionario, funcionario_novo)
    
    @staticmethod
    def modificarMedico(idMedico, medicoNovo):
        return BancoDadosModel.modificarMedico(idMedico, medicoNovo)
    
    
    # @staticmethod
    # def modificarConsulta2(descricao, data, cliente):
    #     return BancoDadosModel.modificarConsulta2(Consulta(descricao, data), cliente)
    
    
    # Delete
    
    @staticmethod
    def deletarCliente(cliente):
        return BancoDadosModel.deletarCliente(cliente)
    
    @staticmethod
    def deletarFuncionario(funcionario):
        return BancoDadosModel.deletarFuncionario(funcionario)
    
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