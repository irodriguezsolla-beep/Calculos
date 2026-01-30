from punto import Punto
from abc import ABC
import math
class Circulo(Punto,ABC):
    def __init__(self,x,y,radio):
        super().__init__(x,y)
        self._radio = radio

    @property
    def Radio(self):
        return self._radio
    @Radio.setter
    def Radio(self,radio):
        self._radio=radio

    def calcularArea(self):
        resultado = math.pi * radio ** 2
        return resultado
