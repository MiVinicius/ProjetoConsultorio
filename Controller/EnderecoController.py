import sys
sys.path.append('.')
from ProjetoConsultorio.Model.EnderecoModel import Endereco



class EnderecoController:

    
    def cadastrarEndereco(self):
        endereco = Endereco(str(input("Digite o nome do Estado: \n")),
                            str(input("Digite o nome da Cidade: \n")),
                            str(input("Digite o nome do Bairro: \n")),
                            str(input("Digite o nome da Rua: \n")),
                            str(input("Digite o número da Casa: \n")),
                            str(input("Digite o CEP: \n"))
                            )
        return endereco
    
    def buscarEndereco(self,pessoa):
        return pessoa._getEndereco()
    
    def atualizarEndereco(self, endereco, pessoa):
        return pessoa._setEndereco(endereco)
    
    def deletarEndereco(self, endereco, pessoa):
        return pessoa._setEndereco(endereco)