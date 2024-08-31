import sys
sys.path.append('.')
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario
from ProjetoConsultorio.Model.ConsultaModel import Consulta
from ProjetoConsultorio.Model.UsuarioModel import Usuario
from ProjetoConsultorio.Model.EnderecoModel import Endereco


class BancoDadosModel():

    
    
    funcionarios :list = []
    medicos :list = []
    clientes :list = []
    consultas :list = []
    usuarios :list = []
    
    @staticmethod
    def _inicializarBase() -> None:
        try:
            endereco = Endereco("SP", "Bauru", "Tomás", "Tomate", "52", "45.450-000")
            cliente = Cliente("George", "123.456.789-00", "8888-8888", endereco)
            BancoDadosModel.cadastrarCliente(cliente)
            consulta = Consulta("Dor de cabeca", "01/01/2022", "10:00", 100, cliente._getCpf())
            BancoDadosModel.cadastrarConsulta(consulta)
            funcionario = Funcionario("Rafael", "456.123.785-00", "9999-9999", endereco, 1000)
            BancoDadosModel.cadastrarFuncionario(funcionario)
            medico = Medico("Carlos", "127.834.566-00", "7777-7777", endereco, 1500, "123456")
            BancoDadosModel.cadastrarMedico(medico)
        except Exception:
            print("Erro ao inicializar o banco de dados")
        return True
    
    # Create
    
    
    def cadastrarUsuario(usuario):
        BancoDadosModel.usuarios.append(usuario)
        return True
    
    
    def cadastrarConsulta(consulta):
        try:
            BancoDadosModel.consultas.append(consulta)
            cliente = consulta._getCliente()
            for cliente_atual in BancoDadosModel.clientes:
                if cliente_atual._getCpf() == cliente:
                    cliente_atual._setConsulta(consulta._getNumero())
                else:
                    return False
            return True
        except Exception as e:
            print("Erro ao cadastrar consulta na Base de dados", e)
            return False
        
        
    
    
    def cadastrarCliente(cliente):
        BancoDadosModel.clientes.append(cliente)
        return True
    
    
    def cadastrarMedico(medico):
        BancoDadosModel.medicos.append(medico)
        return True
    
    
    def cadastrarFuncionario(funcionario):
        BancoDadosModel.funcionarios.append(funcionario)
        return True
    
    # Retreave 
    
    
    def buscarUsuario(usuario:Usuario):
        for usuario in BancoDadosModel.usuarios:
            if usuario.login == usuario.login:
                if usuario.senha == usuario.senha:
                    return True
        return None
    

    def buscarConsulta(numero):
        for consulta_atual in BancoDadosModel.consultas:
            if isinstance(consulta_atual, Consulta):
                if consulta_atual._getNumero() == numero:
                    return consulta_atual
        return None
    
    
    def buscarCliente(cliente):
        for cliente_atual in BancoDadosModel.clientes:
            if isinstance(cliente_atual, Cliente):
                if  cliente_atual._getNome()==cliente._getNome():
                    if cliente_atual._getCpf() == cliente._getCpf():
                        return cliente_atual
        return None
    
    
    def buscarFuncionario(funcionario):
        for funcionario_atual in BancoDadosModel.funcionarios:
            if isinstance(funcionario_atual, Funcionario):
                if  funcionario_atual._getNome()==funcionario._getNome():
                    if funcionario_atual._getCpf() == funcionario._getCpf():
                        return funcionario_atual
        return None
    
    
    def buscarMedico(medico):
        for medico_atual in BancoDadosModel.medicos:
            if isinstance(medico_atual, Medico):
                if  medico_atual._getNome()==medico._getNome():
                    if medico_atual._getCpf() == medico._getCpf():
                        return medico_atual
        return None
    
    # Update
    
    
    def modificarUsuario(clienteAntigo, clienteAtualizado):
        for usuario in BancoDadosModel.usuarios:
            if usuario.login == clienteAntigo.login:
                if usuario.senha == clienteAntigo.senha:
                    usuario.login = clienteAtualizado.login
                    usuario.senha = clienteAtualizado.senha
                    return True
        return False
    
    
    def modificarConsulta(consultaNova:Consulta, consultaModificar:Consulta):
        for consulta in BancoDadosModel.consultas:
            if isinstance(consulta, Consulta):
                if consulta._getNumero() == consultaModificar._getNumero():
                    consulta._setDescricao(consultaNova._getDescricao())
                    consulta._setData(consultaNova._getData())
                    consulta._setHorario(consultaNova._getHorario())
                    consulta._setValor(consultaNova._getValor())
                    print("Cadastro alterado com sucesso")
                    input("pressione ENTER para continuar")
                    return True
            else:
                print("consulta não encontrada")
                return False
        return True
    
    
    def modificarCliente(id_cliente, cliente_novo):
        for cliente in BancoDadosModel.clientes:
            if cliente._getNome() == id_cliente._getNome() and cliente._getCpf() == id_cliente._getCpf():
                cliente._setNome(cliente_novo._getNome())
                cliente._setCpf(cliente_novo._getCpf())
                cliente._setTelefone(cliente_novo._getTelefone())
                cliente._setEndereco(cliente_novo._getEndereco())
                return True
        return False
    
    
    def modificarMedico(id_medico, medico_novo):
        for medico in BancoDadosModel.medicos:
            if medico._getNome() == id_medico._getNome() and medico._getCpf() == id_medico._getCpf():
                medico._setNome(medico_novo._getNome())
                medico._setCpf(medico_novo._getCpf())
                medico._setTelefone(medico_novo._getTelefone())
                medico._setEndereco(medico_novo._getEndereco())
                medico._setSalario(medico_novo._getSalario())
                medico._setCrm(medico_novo._getCrm())
                return True
        return False
    
    
    def modificarFuncionario(id_funcionario, funcionario_novo):
        for funcionario in BancoDadosModel.funcionarios:
            if funcionario._getNome() == id_funcionario._getNome():
                if funcionario._getCpf() == id_funcionario._getCpf():
                    funcionario._setNome(funcionario_novo._getNome())
                    funcionario._setCpf(funcionario_novo._getCpf())
                    funcionario._setTelefone(funcionario_novo._getTelefone())
                    funcionario._setEndereco(funcionario_novo._getEndereco())
                    funcionario._setSalario(funcionario_novo._getSalario())
                    return True
        return False
    
    # Delete
    
    
    def deletarUsuario(usuario):
        BancoDadosModel.usuarios.remove(usuario)
        return True
    
    
    def deletarConsulta(consulta):
        for consulta in BancoDadosModel.consultas:
            if consulta._getNumero() == consulta._getNumero():
                BancoDadosModel.consultas.remove(consulta)
                return True
        print("Consulta não encontrada na lista")
        return False

    
    
    def deletarCliente(cliente):
        BancoDadosModel.clientes.remove(cliente)
        return True
    
    
    def deletarFuncionario(funcionario):
        BancoDadosModel.clientes.remove(funcionario)
        return True
    
    
    def deletarMedico(medico):
        BancoDadosModel.clientes.remove(medico)
        return True
    
    
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
    def mostrarFuncionarios():
        print("Funcionários:")
        for funcionario in BancoDadosModel.funcionarios:
            print(funcionario)
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
            total += consulta._getValor()
        print(f'O valor total dos consultas é: R${total:.2f}')  #retorna o valor total
        input("pressione ENTER para continuar")
    
    
if __name__ == "__main__":
    BancoDadosModel._inicializarBase()
    # BancoDadosModel.mostrarConsultas()
    # BancoDadosModel.mostrarFuncionarios()
    # BancoDadosModel.mostrarMedicos()
    # BancoDadosModel.mostrarClientes()
    BancoDadosModel.valorTotalConsultas()