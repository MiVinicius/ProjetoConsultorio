import sys
sys.path.append('.')
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.AtendenteModel import Atendente
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.EnderecoModel import Endereco


class BancoDadosModel():

    
    
    atendentes :list = []
    medicos :list = []
    clientes :list = []
    consultas :list = []
    usuarios :list = []
    
    @staticmethod
    def _inicializarBase():
        try:
            admin = Usuario("admin", "admin", 0, True)
            BancoDadosModel.cadastrarUsuario(admin)
            endereco = Endereco("SP", "Bauru", "Tomás", "Tomate", "52", "45.450-000")
            cliente = Cliente("George", "123.456.789-00", "8888-8888", endereco)
            BancoDadosModel.cadastrarCliente(cliente)
            consulta = Consulta("Dor de cabeça", "01/01/2022", "10:00", 100, cliente.cpf)
            BancoDadosModel.cadastrarConsulta(consulta)
            atendente = Atendente("Rafael", "456.123.785-00", "9999-9999", endereco, 1000)
            BancoDadosModel.cadastrarAtendente(atendente)
            medico = Medico("Carlos", "127.834.566-00", "7777-7777", endereco, 1500, "123456")
            BancoDadosModel.cadastrarMedico(medico)
        except Exception as e:
            print("Erro ao inicializar o banco de dados", e)
            return False
        return True
    
    # Create
    
    
    def cadastrarUsuario(usuario: Usuario):
        BancoDadosModel.usuarios.append(usuario)
        return True
    
    
    def cadastrarConsulta(consulta: Consulta):
        try:
            BancoDadosModel.consultas.append(consulta)
            cliente = consulta.cliente
            for cliente_atual in BancoDadosModel.clientes:
                if cliente_atual.cpf == cliente:
                    cliente_atual.consulta = consulta.numero
                else:
                    return False
            return True
        except Exception as e:
            print("Erro ao cadastrar consulta na Base de dados", e)
            return False
        
        
    
    
    def cadastrarCliente(cliente: Cliente):
        BancoDadosModel.clientes.append(cliente)
        return True
    
    
    def cadastrarMedico(medico: Medico):
        BancoDadosModel.medicos.append(medico)
        return True
    
    
    def cadastrarAtendente(atendente: Atendente):
        BancoDadosModel.atendentes.append(atendente)
        return True
    
    # Retreave 
    
    
    def buscarUsuario(usuario:Usuario):
        for usuario_atual in BancoDadosModel.usuarios:
            if usuario_atual.login == usuario.login:
                if usuario_atual.senha == usuario.senha:
                    if usuario_atual.tipo == usuario.tipo:
                        return usuario_atual
        return None
    

    def buscarConsulta(numero):
        for consulta_atual in BancoDadosModel.consultas:
            if isinstance(consulta_atual, Consulta):
                if consulta_atual.numero == numero:
                    return consulta_atual
        return None
    
    
    def buscarCliente(cliente: Cliente):
        for cliente_atual in BancoDadosModel.clientes:
            if isinstance(cliente_atual, Cliente):
                if  cliente_atual.nome==cliente.nome:
                    if cliente_atual.cpf == cliente.cpf:
                        return cliente_atual
        return None
    
    
    def buscarAtendente(atendente: Atendente):
        for atendente_atual in BancoDadosModel.atendentes:
            if isinstance(atendente_atual, Atendente):
                if  atendente_atual.nome==atendente.nome:
                    if atendente_atual.cpf == atendente.cpf:
                        return atendente_atual
        return None
    
    
    def buscarMedico(medico: Medico):
        for medico_atual in BancoDadosModel.medicos:
            if isinstance(medico_atual, Medico):
                if  medico_atual.nome==medico.nome:
                    if medico_atual.cpf == medico.cpf:
                        return medico_atual
        return None
    
    # Update
    
    
    def modificarUsuario(usuarioAntigo, usuarioAtualizado):
        for usuario_atual in BancoDadosModel.usuarios:
            if usuario_atual.login == usuarioAntigo.login:
                if usuario_atual.senha == usuarioAntigo.senha:
                    usuario_atual.login = usuarioAtualizado.login
                    usuario_atual.senha = usuarioAtualizado.senha
                    return True
        return False
    
    
    def modificarConsulta(consultaNova:Consulta, consultaModificar:Consulta):
        for consulta_atual in BancoDadosModel.consultas:
            if isinstance(consulta_atual, Consulta):
                if consulta_atual.numero == consultaModificar.numero:
                    consulta_atual.descricao = consultaNova.descricao
                    consulta_atual.data = consultaNova.data
                    consulta_atual.horario = consultaNova.horario
                    consulta_atual.valor = consultaNova.valor
                    print("Cadastro alterado com sucesso")
                    input("pressione ENTER para continuar")  # lembrar de tirar daqui e colocar em outro lugar
                    return True
            else:
                print("consulta não encontrada")
                return False
        return True
    
    
    def modificarCliente(id_cliente, cliente_novo):
        for cliente in BancoDadosModel.clientes:
            if cliente.nome == id_cliente.nome and cliente.cpf == id_cliente.cpf:
                cliente.nome = cliente_novo.nome
                cliente.cpf = cliente_novo.cpf
                cliente.telefone = cliente_novo.telefone
                cliente.endereco = cliente_novo.endereco
                return True
        return False
    
    
    def modificarMedico(id_medico, medico_novo):
        for medico in BancoDadosModel.medicos:
            if medico.nome == id_medico.nome and medico.cpf == id_medico.cpf:
                medico.nome = medico_novo.nome
                medico.cpf = medico_novo.cpf
                medico.telefone = medico_novo.telefone
                medico.endereco = medico_novo.endereco
                medico.salario = medico_novo.salario
                medico.crm = medico_novo.crm
                return True
        return False
    
    
    def modificarAtendente(id_atendente, atendente_novo):
        for atendente in BancoDadosModel.atendentes:
            if atendente.nome == id_atendente.nome:
                if atendente.cpf == id_atendente.cpf:
                    atendente.nome = atendente_novo.nome
                    atendente.cpf = atendente_novo.cpf
                    atendente.telefone = atendente_novo.telefone
                    atendente.endereco = atendente_novo.endereco
                    atendente.salario = atendente_novo.salario
                    return True
        return False
    
    # Delete
    
    
    def deletarUsuario(usuario):
        for Usuario_atual in BancoDadosModel.usuarios:
            if isinstance(Usuario_atual, Usuario):
                if Usuario_atual.login == usuario.login:
                    if Usuario_atual.senha == usuario.senha:
                        BancoDadosModel.usuarios.remove(Usuario_atual)
                        return True
        return False
    
    
    def deletarConsulta(consulta):
        for consulta_atual in BancoDadosModel.consultas:
            if consulta_atual.numero == consulta:
                BancoDadosModel.consultas.remove(consulta_atual)
                return True
        print("Consulta não encontrada na lista")
        return False

    
    
    def deletarCliente(cliente):
        for cliente_atual in BancoDadosModel.clientes:
            if isinstance(cliente_atual, Cliente):
                if cliente_atual.nome == cliente.nome:
                    if cliente_atual.cpf == cliente.cpf:
                        BancoDadosModel.clientes.remove(cliente_atual)
                        return True
        return False
    
    
    def deletarAtendente(atendente):
        for atendente_atual in BancoDadosModel.atendentes:
            if isinstance(atendente_atual, Atendente):
                if atendente_atual.nome == atendente.nome:
                    if atendente_atual.cpf == atendente.cpf:
                        BancoDadosModel.atendentes.remove(atendente_atual)
                        return True
        return False
    
    
    def deletarMedico(medico):
        for medico_atual in BancoDadosModel.medicos:
            if isinstance(medico_atual, Medico):
                if medico_atual.nome == medico.nome:
                    if medico_atual.cpf == medico.cpf:
                        BancoDadosModel.medicos.remove(medico_atual)
                        return True
        return False
    
    
    # métodos adicionais
    
    @staticmethod
    def mostrarClientes():
        print("Clientes:")
        for cliente in BancoDadosModel.clientes:
            print(cliente)
        input("pressione ENTER para continuar")
    
    @staticmethod
    def mostrarMedicos():
        print("Medicos:")
        for medico in BancoDadosModel.medicos:
            print(medico)
        input("pressione ENTER para continuar")
            
    @staticmethod
    def mostrarAtendentes():
        print("Atendentes:")
        for atendente_atual in BancoDadosModel.atendentes:
            print(atendente_atual)
        input("pressione ENTER para continuar")
            
    @staticmethod
    def mostrarConsultas():
        print("Consultas Cadastradas:")
        for consulta in BancoDadosModel.consultas:
            print(consulta.__str__())
            print()
        input("pressione ENTER para continuar")
        
    @staticmethod
    def valorTotalConsultas():
        total = 0
        print("Consultas Cadastradas:")
        for consulta in BancoDadosModel.consultas:
            total += consulta.valor
        print(f'O valor total dos consultas é: R${total:.2f}')  #retorna o valor total
        input("pressione ENTER para continuar")
    
    
