import sys
sys.path.append('.')
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.EnderecoModel import Endereco


class BancoDadosModel:

    def __init__(self) -> None:
        self.atendentes: list[Atendente] = []
        self.medicos: list[Medico] = []
        self.clientes: list[Cliente] = []
        self.consultas: list[Consulta] = []
        self.usuarios: list[Usuario] = []
        self._inicializarBase()
    
    def _inicializarBase(self):
        try:
            endereco = Endereco("SP", "Bauru", "Tomás", "Tomate", "52", "45.450-000")
            admin = Usuario("admin", "admin", 0, True)
            self.cadastrarUsuario(admin)
            cliente = Cliente("George", "123.456.789-00", "8888-8888", endereco)
            self.cadastrarCliente(cliente)
            consulta = Consulta("Dor de cabeça", "01/01/2022", "10:00", 100, cliente.cpf)
            self.cadastrarConsulta(consulta)
            atendente = Atendente("Rafael", "456.123.785-00", "9999-9999", endereco, 1000)
            self.cadastrarAtendente(atendente)
            medico = Medico("Carlos", "127.834.566-00", "7777-7777", endereco, 1500, "123456")
            self.cadastrarMedico(medico)
        except Exception as e:
            print("Erro ao inicializar o banco de dados:", e)
            return False
        return True
    
    # Create
    def cadastrarUsuario(self, usuario: Usuario):
        if not any(u.login == usuario.login for u in self.usuarios):
            self.usuarios.append(usuario)
            return True
        return False
    
    def cadastrarConsulta(self, consulta: Consulta):
        try:
            cliente = next((c for c in self.clientes if c.cpf == consulta.cliente), None)
            if cliente:
                self.consultas.append(consulta)
                cliente.consulta = consulta.numero
                return True
            return False
        except Exception as e:
            print("Erro ao cadastrar consulta na Base de dados:", e)
            return False
    
    def cadastrarCliente(self, cliente: Cliente):
        if not any(c.cpf == cliente.cpf for c in self.clientes):
            self.clientes.append(cliente)
            return True
        return False
    
    def cadastrarMedico(self, medico: Medico):
        if not any(m.cpf == medico.cpf for m in self.medicos):
            self.medicos.append(medico)
            return True
        return False
    
    def cadastrarAtendente(self, atendente: Atendente):
        if not any(a.cpf == atendente.cpf for a in self.atendentes):
            self.atendentes.append(atendente)
            return True
        return False
    
    # Retrieve
    def buscarUsuario(self, usuario: Usuario):
        return next((u for u in self.usuarios if u.login == usuario.login and u.senha == usuario.senha and u.tipo == usuario.tipo), None)
    
    def buscarConsulta(self, numero):
        return next((consulta for consulta in self.consultas if consulta.numero == numero), None)
    
    def buscarCliente(self, cliente: Cliente):
        return next((c for c in self.clientes if c.nome == cliente.nome and c.cpf == cliente.cpf), None)
    
    def buscarAtendente(self, atendente: Atendente):
        return next((a for a in self.atendentes if a.nome == atendente.nome and a.cpf == atendente.cpf), None)
    
    def buscarMedico(self, medico: Medico):
        return next((m for m in self.medicos if m.nome == medico.nome and m.cpf == medico.cpf), None)
    
    # Update
    def modificarUsuario(self, usuarioAntigo: Usuario, usuarioAtualizado: Usuario):
        usuario = self.buscarUsuario(usuarioAntigo)
        if usuario:
            usuario.login = usuarioAtualizado.login
            usuario.senha = usuarioAtualizado.senha
            usuario.tipo = usuarioAtualizado.tipo
            return True
        return False
    
    def modificarConsulta(self, consultaNova: Consulta, consultaModificar: Consulta):
        consulta = self.buscarConsulta(consultaModificar.numero)
        if consulta:
            consulta.descricao = consultaNova.descricao
            consulta.data = consultaNova.data
            consulta.horario = consultaNova.horario
            consulta.valor = consultaNova.valor
            return True
        return False
    
    def modificarCliente(self, id_cliente: Cliente, cliente_novo: Cliente):
        cliente = self.buscarCliente(id_cliente)
        if cliente:
            cliente.nome = cliente_novo.nome
            cliente.cpf = cliente_novo.cpf
            cliente.telefone = cliente_novo.telefone
            cliente.endereco = cliente_novo.endereco
            return True
        return False
    
    def modificarMedico(self, id_medico: Medico, medico_novo: Medico):
        medico = self.buscarMedico(id_medico)
        if medico:
            medico.nome = medico_novo.nome
            medico.cpf = medico_novo.cpf
            medico.telefone = medico_novo.telefone
            medico.endereco = medico_novo.endereco
            medico.salario = medico_novo.salario
            medico.crm = medico_novo.crm
            return True
        return False
    
    def modificarAtendente(self, id_atendente: Atendente, atendente_novo: Atendente):
        atendente = self.buscarAtendente(id_atendente)
        if atendente:
            atendente.nome = atendente_novo.nome
            atendente.cpf = atendente_novo.cpf
            atendente.telefone = atendente_novo.telefone
            atendente.endereco = atendente_novo.endereco
            atendente.salario = atendente_novo.salario
            return True
        return False
    
    # Delete
    def deletarUsuario(self, usuario: Usuario):
        usuario_a_remover = self.buscarUsuario(usuario)
        if usuario_a_remover:
            self.usuarios.remove(usuario_a_remover)
            return True
        return False
    
    def deletarConsulta(self, numero_consulta):
        consulta_a_remover = self.buscarConsulta(numero_consulta)
        if consulta_a_remover:
            self.consultas.remove(consulta_a_remover)
            return True
        print("Consulta não encontrada na lista")
        return False
    
    def deletarCliente(self, cliente: Cliente):
        cliente_a_remover = self.buscarCliente(cliente)
        if cliente_a_remover:
            self.clientes.remove(cliente_a_remover)
            return True
        return False
    
    def deletarAtendente(self, atendente: Atendente):
        atendente_a_remover = self.buscarAtendente(atendente)
        if atendente_a_remover:
            self.atendentes.remove(atendente_a_remover)
            return True
        return False
    
    def deletarMedico(self, medico: Medico):
        medico_a_remover = self.buscarMedico(medico)
        if medico_a_remover:
            self.medicos.remove(medico_a_remover)
            return True
        return False
    
    # Métodos adicionais
    def mostrarClientes(self):
        print("Clientes:")
        for cliente in self.clientes:
            print(cliente, end='\n\n')

    def mostrarMedicos(self):
        print("Médicos:")
        for medico in self.medicos:
            print(medico, end='\n\n')

    def mostrarAtendentes(self):
        print("Atendentes:")
        for atendente in self.atendentes:
            print(atendente, end='\n\n')

    def mostrarConsultas(self):
        print("Consultas Cadastradas:")
        for consulta in self.consultas:
            print(consulta, end='\n\n')

    def valorTotalConsultas(self):
        total = sum(consulta.valor for consulta in self.consultas)
        print(f'O valor total das consultas é: R${total:.2f}')

    
