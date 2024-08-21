class Endereco:
    def __init__(self, cidade, cep, bairro, rua, numero):
        self.cidade = cidade
        self.cep = cep
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

class Consulta:
    def __init__(self, nomePaciente, idadePaciente, sintomas):
        self.nomePaciente = nomePaciente
        self.idadePaciente = idadePaciente
        self.sintomas = sintomas 
        
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, endereco):
        super().__init__(nome, idade, cpf)
        self.email = email
        self.endereco = endereco
        
class Funcionario (Pessoa):
    def __init__(self, nome, idade, cpf, salario, contrato):
        super().__init__(nome, idade, cpf)
        self.salario = salario
        self.contrato = contrato

class Atendente (Funcionario):
    def __init__(self, nome, idade, cpf, salario, contrato):
        super().__init__(nome, idade, cpf, salario, contrato)

class Medico (Funcionario):
    def __init__(self, nome, idade, cpf, salario, contrato,):
        super().__init__(nome, idade, cpf, salario, contrato) 
        