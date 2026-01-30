from bastracto2 import Terrestre
class CocheAutonomo(Terrestre):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numeroRodas, numeroPrazas):
        super().__init__(matricula,velocidadeMaxima,autonomia,numeroRodas)
        self.numeroPrazas = numeroPrazas

    @property
    def numeroPrazas(self):
        return self._numeroPrazas
    @numeroPrazas.setter
    def numeroPrazas(self,numeroPrazas):
        self._numeroPrazas = numeroPrazas

    def arrincar(self):
        print(f"O coche autonomo arrinca")
    def mostrardatos(self):
        print(f"La matricula: {self._matricula}, VelocidadMaxima: {self._velocidadeMaxima}, Autonimia: {self._autonomia}, Número de rodas: {self._numero_rodas}, Numero de prazas: {self._numeroPrazas} ")


coche = CocheAutonomo(1231,234,123,4,5)

print(coche.mostrardatos())