import sys
sys.path.append('.')
from ProjetoCadastro.Model.EnderecoModel import Endereco

class EnderecoController:
    
    @staticmethod
    def cadastrarEndereco():
        endereco = Endereco(str(input("Digite o nome do Estado: \n")),
                            str(input("Digite o nome da Cidade: \n")),
                            int(input("Digite o nome do Bairro: \n")),
                            str(input("Digite o nome da Rua: \n")),
                            str(input("Digite o número da Casa: \n")))
        return endereco
    
    @staticmethod
    def buscarEndereco(pessoa):
        return pessoa._getEndereco()
    
    @staticmethod
    def atualizarEndereco(endereco, pessoa):
        return pessoa._setEndereco(endereco)
    
    @staticmethod
    def deletarEndereco(endereco, pessoa):
        return pessoa._setEndereco(endereco)