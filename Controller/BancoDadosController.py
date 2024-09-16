import sys
sys.path.append('.')

from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente
from ProjetoConsultorio.Model.BancoDadosModel import BancoDadosModel



class BancoDadosController:
    
    def __init__(self):
        self.model = BancoDadosModel("Consultorio.db")

    # Create
    def cadastrarUsuario(self, login, senha, tipo):
        return self.model.cadastrarUsuario(Usuario(login, senha, tipo))
        
    def cadastrarCliente(self, nome, cpf, DataNasc, telefone, endereco):
        return self.model.cadastrarCliente(Cliente(nome, cpf, DataNasc, telefone, None), endereco)
    
    def cadastrarConsulta(self, descricao, data, horario, valor, cliente, medico):
        return self.model.cadastrarConsulta(Consulta(descricao, data, horario, valor, cliente, medico))
    
    def cadastrarAtendente(self, nome, cpf, DataNasc, telefone, salario, endereco):
        return self.model.cadastrarAtendente(Atendente(nome, cpf, DataNasc, telefone, None, salario), endereco)
    
    def cadastrarMedico(self, nome, cpf, DataNasc, telefone, salario, crm, endereco):
        return self.model.cadastrarMedico(Medico(nome, cpf, DataNasc, telefone, None, salario, crm), endereco)
    
    # Retreave
    def buscarUsuario(self, login, senha, tipo):
        return self.model.buscarUsuario(Usuario(login, senha, tipo, False))
        
    def buscarCliente(self, nome, cpf):
        return self.model.buscarCliente(nome, cpf)
    
    def buscarConsulta(self, numero):
        return self.model.buscarConsulta(numero)
    
    def buscarListaConsulta(self, cliente_id):
        return self.model.buscarListaConsulta(cliente_id)
    
    def buscarAtendente(self, nome, cpf):
        return self.model.buscarAtendente(nome, cpf)
    
    def buscarMedico(self, nome, cpf):
        return self.model.buscarMedico(nome, cpf)
    
    # Update
    def modificarUsuario(self, usuario, login, senha, tipo):
        return self.model.modificarUsuario(usuario, Usuario(login, senha, tipo))
    
    def modificarCliente(self, clienteAntigo, nome, cpf, DataNasc, telefone):
        return self.model.modificarCliente(clienteAntigo, Cliente(nome, cpf, DataNasc, telefone, None))
    
    def modificarConsulta(self, descricao, data, horario, valor, cliente, medico, consultaModificar):
        return self.model.modificarConsulta(consultaModificar, Consulta(descricao, data, horario, valor, cliente, medico))
    
    def modificarAtendente(self, atendente_existe, nomeNovo, cpfAntigo, DataNascNovo, telefoneNovo, salarioNovo):
        return self.model.modificarAtendente(atendente_existe, Atendente(nomeNovo, cpfAntigo, DataNascNovo, telefoneNovo, None, salarioNovo))
    
    def modificarMedico(self, medicoAntigo, nomeNovo, cpfAntigo, DataNascNovo, telefoneNovo, salarioNovo, crmNovo):
        return self.model.modificarMedico(medicoAntigo, Medico(nomeNovo, cpfAntigo, DataNascNovo, telefoneNovo, None, salarioNovo, crmNovo))
    
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
    
    def atualizar_endereco(self, enderecoExistente, novoEndereco):
        return self.model.atualizarEndereco(enderecoExistente, novoEndereco)

    def mostrar_consultas(self):
        return self.model.obterTodasConsultas()
    
    def valorTotalConsultas(self):
        return self.model.calcularValorTotalConsultas()
    
    def mostrarAtendentes(self):
        return self.model.obterTodosAtendentes()
    
    def mostrarClientes(self):
        return self.model.obterTodosClientes()
    
    def mostrarMedicos(self):
        return self.model.obterTodosMedicos()

    
