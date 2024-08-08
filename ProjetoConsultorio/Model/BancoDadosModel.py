import sys
sys.path.append('.')
from ProjetoConsultorio.Model.ClienteModel import Cliente
from ProjetoConsultorio.Model.MedicoModel import Medico
from ProjetoConsultorio.Model.FuncionarioModel import Funcionario


class BancoDadosModel():
    
    funcionarios :list = []
    medicos :list = []
    clientes :list = []
    consultas :list = []
    
    @staticmethod
    def _inicializarBase() -> None:
        cliente = Cliente("George", "12345678")
        BancoDadosModel.cadastrarCliente(cliente) 
        return True
    
    @staticmethod
    def cadastrarConsulta(consulta):
        BancoDadosModel.consultas.append(consulta)
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
    
    @staticmethod
    def buscarConsulta(consulta):
        for consulta_atual in BancoDadosModel.consultas:
            if consulta_atual.descricao == consulta.descricao:
                if consulta_atual.data == consulta.data:
                    return consulta_atual
    
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
    
    @staticmethod
    def modificarConsulta(consulta, consulta_nova):
        for consulta_atual in BancoDadosModel.consultas:
            if consulta_atual.getDescricao() == consulta.getDescricao():
                if consulta_atual.getData() == consulta.getData():
                    BancoDadosModel.consultas.index(consulta_atual).setDescricao(consulta_nova.getDescricao())
                    BancoDadosModel.consultas.index(consulta_atual).setData(consulta_nova.getData())
                    return True
        return False
    
    @staticmethod
    def modificarCliente(id_cliente, cliente_novo):
        for cliente in BancoDadosModel.clientes:
            if cliente._getNome() == id_cliente._getNome():
                if cliente._getCpf() == id_cliente._getCpf():
                    BancoDadosModel.clientes.index(cliente)._setNome(cliente_novo._getNome())
                    BancoDadosModel.clientes.index(cliente)._setCpf(cliente_novo._getCpf())
                    return True
        return False
    
    @staticmethod
    def modificarMedico(id_medico, medico_novo):
        for medico in BancoDadosModel.medicos:
            if medico._getNome() == id_medico._getNome():
                if medico._getCpf() == id_medico._getCpf():
                    BancoDadosModel.medicos.index(medico)._setNome(medico_novo._getNome())
                    BancoDadosModel.medicos.index(medico)._setCpf(medico_novo._getCpf())
                    return True
        return False
    
    @staticmethod
    def modificarFuncionario(id_funcionario, funcionario_novo):
        for funcionario in BancoDadosModel.funcionarios:
            if funcionario._getNome() == id_funcionario._getNome():
                if funcionario._getCpf() == id_funcionario._getCpf():
                    BancoDadosModel.clientes.index(funcionario)._setNome(funcionario_novo._getNome())
                    BancoDadosModel.clientes.index(funcionario)._setCpf(funcionario_novo._getCpf())
                    return True
        return False
    
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
            print(consulta)
    
if __name__ == "__main__":
    BancoDadosModel._inicializarBase()
    BancoDadosModel.mostrarClientes()