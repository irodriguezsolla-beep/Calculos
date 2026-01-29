from bastracto import Vehiculo
from abc import ABC, abstractmethod
class Aereo(Vehiculo,ABC):
    def __init__(self,matricula,velocidadeMaxima,autonomia,AltitudeMaxima):
        super().__init__(matricula,velocidadeMaxima,autonomia)
        self.altitude_maxima = AltitudeMaxima

    @property
    def AltitudeMaxima(self):
        return self._altitude_maxima
    @numero_rodas.setter
    def numero_rodas(self,AltitudeMaxima):
        self._altitude_maxima= AltitudeMaxima