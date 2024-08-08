class Endereco():
    def Endereco(self, estado, cidade, bairro, numero):
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__numero = numero
    
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
        
    def _getNumero(self):
        return self.__numero
    
    def _setNumero(self, numero):
        self.__numero = numero
        
    def __repr__(self) -> str:
        return f"Rua: {self.__rua}, Bairro: {self.__bairro}, Número: {self.__numero}, Cidade: {self.__cidade}, Estado: {self.__estado}"
          
    