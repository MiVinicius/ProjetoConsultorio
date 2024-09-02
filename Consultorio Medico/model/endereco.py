class Endereco:
    def __init__(self, cidade, rua, bairro, cep, numero):
        self.__cidade = cidade
        self.__rua = rua
        self.__bairro = bairro
        self.__cep = cep
        self.__numero = numero

    @property
    def cidade(self):
        return self.__cidade

    @property
    def rua(self):
        return self.__rua

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cep(self):
        return self.__cep

    @property
    def numero(self):
        return self.__numero

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}, {self.cep}"
