class Consulta:
    
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data
        
    def _getDescricao(self):
        return self.descricao
    def _setDescricao(self, descricao):
        self.descricao = descricao
    def _getData(self):
        return self.data
    def _setDescricao(self, data):
        self.data = data       
        