from model_funcionario import ModelFuncionario
from model_medico import ModelMedico
from model_atendente import ModelAtendente

class ModelAdministrador(ModelFuncionario):
    def __init__(self, nome, cpf, endereco, telefone, login, senha, salario):
        super().__init__(nome, cpf, endereco, telefone, login, senha, salario, "Administrador")

    def criar_funcionario(self, tipo, **kwargs):
        if tipo == "Medico":
            return ModelMedico(**kwargs)
        elif tipo == "Atendente":
            return ModelAtendente(**kwargs)
        elif tipo == "Administrador":
            return ModelAdministrador(**kwargs)
        else:
            raise ValueError("Tipo de funcionário inválido!")

    def editar_funcionario(self, funcionario, **novos_dados):
        for key, value in novos_dados.items():
            if hasattr(funcionario, key):
                setattr(funcionario, key, value)
            else:
                print(f"Atributo {key} não encontrado no funcionário.")

    def remover_funcionario(self, banco_de_dados, funcionario):
        if isinstance(funcionario, ModelMedico):
            banco_de_dados.medicos.remove(funcionario)
        elif isinstance(funcionario, ModelAtendente):
            banco_de_dados.atendentes.remove(funcionario)
        elif isinstance(funcionario, ModelAdministrador):
            banco_de_dados.administradores.remove(funcionario)
        else:
            raise ValueError("Tipo de funcionário inválido!")

    def criar_administrador(self, banco_de_dados, nome, cpf, endereco, telefone, login, senha, salario):
        novo_admin = ModelAdministrador(nome, cpf, endereco, telefone, login, senha, salario)
        banco_de_dados.administradores.append(novo_admin)
        print(f"Administrador {nome} criado com sucesso.")

    def editar_administrador(self, administrador, **novos_dados):
        self.editar_funcionario(administrador, **novos_dados)
        print(f"Administrador {administrador.nome} editado com sucesso.")

    def remover_administrador(self, banco_de_dados, administrador):
        self.remover_funcionario(banco_de_dados, administrador)
        print(f"Administrador {administrador.nome} removido com sucesso.")
