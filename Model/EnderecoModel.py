import sys
sys.path.append('.')
class Endereco():
    
    def __init__(self, estado, cidade, bairro, rua, numero, cep):
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__cep = cep
    
    def _getEstado(self):
        return self.__estado
    
    def _setEstado(self, estado):
        self.__estado = estado
        
    def _getCidade(self):
        return self.__cidade
    
    def _setCidade(self, cidade):
        self.__cidade = cidade
        
    def _getBairro(self):
        return self.__bairro
    
    def _setBairro(self, bairro):
        self.__bairro = bairro
        
    def _getRua(self):
        return self.__rua
    
    def _setRua(self, rua):
        self.__rua = rua
        
    def _getNumero(self):
        return self.__numero
    
    def _setNumero(self, numero):
        self.__numero = numero
        
    def _getCep(self):
        return self.__cep
    
    def _setCep(self, cep):
        self.__cep = cep
        
    def __repr__(self) -> str:
        return f"Rua: {self.__rua}, Bairro: {self.__bairro}, Número: {self.__numero}, CEP: {self.__cep}, Cidade: {self.__cidade}, Estado: {self.__estado}"
    