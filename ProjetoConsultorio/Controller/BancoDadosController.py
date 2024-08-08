from Model.BancoDadosModel import BancoDadosModel


class BancoDadosController():
    
    @staticmethod
    def inicializarBase():
        BancoDadosModel._inicializarBase()
        
    @staticmethod
    def cadastrarCliente(cliente):
        return BancoDadosModel.cadastrarCliente(cliente)
    
    @staticmethod
    def cadastrarConsulta(consulta):
        return BancoDadosModel.cadastrarConsulta(consulta)
    
    @staticmethod
    def buscarCliente(cliente):
        return BancoDadosModel.buscarCliente(cliente)
    
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