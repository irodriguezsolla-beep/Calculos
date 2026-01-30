from circulo import Circulo
import math
class Cilindro(Circulo):
    def __init__(self,x,y,radio,altura):
        super().__init__(x,y,radio)
        self._altura = altura

    @property
    def Altura(self):
        return self._altura
    @Altura.setter
    def Altura(self,altura):
        self._altura= altura

    def __str__(self):
        return (f"El punto es: {self._x},{self._y}  | El radio es:{self._radio} | La altura es: {self._altura}")
    def calcularArea(self):
        area = 2 * math.pi * self._radio *(self._radio + self._altura)
        return area
    def calcularVolumen(self):
        volumen = math.pi * self._altura * self._radio ** 2
        return volumen

cil = Cilindro(2,4,28,45)
print(cil.calcularVolumen())