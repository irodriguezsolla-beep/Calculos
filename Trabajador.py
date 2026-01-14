from Persoa2 import persoa

class trabajador(persoa):
    def __init__(self,nome,dni,idade,NUSS):
        super().__init__(nome,dni,idade)
        self.setNUSS(NUSS)

    def setNUSS(self,NUSS):
