from bastracto import Vehiculo
from abc import ABC
class Terrestre(Vehiculo,ABC):
    def __init__(self,matricula,velocidadeMaxima,autonomia,numeroRodas):
        super().__init__(matricula,velocidadeMaxima,autonomia)
        self.numero_rodas = numeroRodas

    @property
    def numero_rodas(self):
        return self._numero_rodas
    @numero_rodas.setter
    def numero_rodas(self,numeroRodas):
        self._numero_rodas= numeroRodas