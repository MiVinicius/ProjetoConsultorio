import sys
sys.path.append('.')
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario
from ProjetoConsultorio.Model.ConsultaModel import Consulta


class BancoDadosModel():

    
    
    funcionarios :list = []
    medicos :list = []
    clientes :list = []
    consultas :list = []
    usuarios :list = []
    
    
    @staticmethod
    def _inicializarBase() -> None:
        try:
            cliente = Cliente("George", "12345678")
            BancoDadosModel.cadastrarCliente(cliente)
            consulta = Consulta("Dor de cabeca", "01/01/2022")
            BancoDadosModel.cadastrarConsulta(consulta)
            funcionario = Funcionario("Rafael", "12345678")
            BancoDadosModel.cadastrarFuncionario(funcionario)
            medico = Medico("Carlos", "12345678")
            BancoDadosModel.cadastrarMedico(medico)
        except Exception:
            print("Erro ao inicializar o banco de dados")
        return True
    
    # Create
    
    @staticmethod
    def cadastrarUsuario(usuario):
        BancoDadosModel.usuarios.append(usuario)
        return True
    
    @staticmethod
    def cadastrarConsulta(consulta):
        BancoDadosModel.consultas.append(consulta)
        cliente = consulta._getCliente()
        for consultaAtual in BancoDadosModel.consultas:
            if consultaAtual.getNumero() == consulta.getNumero():
                cliente._setConsulta(consulta)
            else:
                return False
        return True
    
    @staticmethod
    def cadastrarCliente(cliente):
        BancoDadosModel.clientes.append(cliente)
        return True
    
    @staticmethod
    def cadastrarMedico(medico):
        BancoDadosModel.medicos.append(medico)
        return True
    
    @staticmethod
    def cadastrarFuncionario(funcionario):
        BancoDadosModel.funcionarios.append(funcionario)
        return True
    
    # Retreave 
    
    @staticmethod
    def buscarUsuario(usuario):
        for usuario in BancoDadosModel.usuarios:
            if usuario.login == usuario.login:
                if usuario.senha == usuario.senha:
                    return True
        return None
    
    @staticmethod       # provavelmente funciona
    def buscarConsulta(numero):
        for consulta_atual in BancoDadosModel.consultas:
            if consulta_atual.numero == numero:
                return consulta_atual
        return None
    
    @staticmethod
    def buscarCliente(cliente):
        for cliente_atual in BancoDadosModel.clientes:
            if isinstance(cliente_atual, Cliente):
                if  cliente_atual._getNome()==cliente._getNome():
                    if cliente_atual._getCpf() == cliente._getCpf():
                        return cliente_atual
        return None
    
    @staticmethod
    def buscarFuncionario(funcionario):
        for funcionario_atual in BancoDadosModel.funcionarios:
            if isinstance(funcionario_atual, Funcionario):
                if  funcionario_atual._getNome()==funcionario._getNome():
                    if funcionario_atual._getCpf() == funcionario._getCpf():
                        return funcionario_atual
        return None
    
    @staticmethod
    def buscarMedico(medico):
        for medico_atual in BancoDadosModel.medicos:
            if isinstance(medico_atual, Medico):
                if  medico_atual._getNome()==medico._getNome():
                    if medico_atual._getCpf() == medico._getCpf():
                        return medico_atual
        return None
    
    # Update
    
    @staticmethod
    def modificarConsulta(consultaNova:Consulta, consultaModificar:Consulta):
        for consulta in BancoDadosModel.consultas:
            if isinstance(consulta, Consulta):
                if consulta.getNumero() == consultaModificar.getNumero():
                    print(f"consulta encontrada: {consulta.getNumero()} - {consultaModificar.getNumero()}")
                    consulta._setDescricao(consultaNova._getDescricao())
                    print(f"consulta modificada: {consulta._getDescricao()} - {consultaModificar._getDescricao()}")
                    consulta._setData(consultaNova._getData())
                    print(f"consulta modificada: {consulta._getData()} - {consultaModificar._getData()}")
            else:
                return print("consulta não encontrada")
        return True
    
    @staticmethod
    def modificarCliente(id_cliente, cliente_novo):
        for cliente in BancoDadosModel.clientes:
            if cliente._getNome() == id_cliente._getNome() and cliente._getCpf() == id_cliente._getCpf():
                cliente._setNome(cliente_novo._getNome())
                cliente._setCpf(cliente_novo._getCpf())
            return True
        return False
    
    @staticmethod
    def modificarMedico(id_medico, medico_novo):
        for medico in BancoDadosModel.medicos:
            if medico._getNome() == id_medico._getNome() and medico._getCpf() == id_medico._getCpf():
                medico._setNome(medico_novo._getNome())
                medico._setCpf(medico_novo._getCpf())
                return True
        return False
    
    @staticmethod
    def modificarFuncionario(id_funcionario, funcionario_novo):
        for funcionario in BancoDadosModel.funcionarios:
            if funcionario._getNome() == id_funcionario._getNome():
                if funcionario._getCpf() == id_funcionario._getCpf():
                    funcionario._setNome(funcionario_novo._getNome())
                    funcionario._setCpf(funcionario_novo._getCpf())
                    return True
        return False
    
    # Delete
    
    @staticmethod
    def deletarConsulta(consulta):
        BancoDadosModel.consultas.remove(consulta)
        return True
    
    @staticmethod
    def deletarCliente(cliente):
        BancoDadosModel.clientes.remove(cliente)
        return True
    
    @staticmethod
    def deletarFuncionario(funcionario):
        BancoDadosModel.clientes.remove(funcionario)
        return True
    
    @staticmethod
    def deletarMedico(medico):
        BancoDadosModel.clientes.remove(medico)
        return True
    
    
    # métodos adicionais
    
    @staticmethod
    def mostrarClientes():
        for cliente in BancoDadosModel.clientes:
            print(cliente)
    
    @staticmethod
    def mostrarMedicos():
        for medico in BancoDadosModel.medicos:
            print(medico)
            
    @staticmethod
    def mostrarFuncionarios():
        for funcionario in BancoDadosModel.funcionarios:
            print(funcionario)
            
    @staticmethod
    def mostrarConsultas():
        for consulta in BancoDadosModel.consultas:
            print(consulta.__str__())
        
    @staticmethod
    def valorTotalConsultas():
        total = 0
        for consulta in BancoDadosModel.consultas:
            total += consulta.getValor()
        return f'R${total:.2f}' #retorna o valor total
    
