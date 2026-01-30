from abc import ABC, abstractmethod
class Vehiculo(ABC):
    def __init__(self,matricula,velocidadeMaxima,autonomia):
        self.setMatricula(matricula)
        self.setVelocidad(velocidadeMaxima)
        self.setAutonomia(autonomia)

    def setMatricula(self,matricula):
         self._matricula = matricula
    def getMatricula(self):
        return  self._matricula

    def setVelocidad(self, velocidadeMaxima):
        self._velocidadeMaxima = velocidadeMaxima
    def getVelocidad(self):
        return self._velocidadeMaxima

    def setAutonomia(self,autonimia):
         self._autonomia = autonimia
    def getAutonomia(self):
        return  self._autonomia

    def __str__(self):
        return (f"Matricula: {self._matricula}, Velocidade:{self._velocidadeMaxima}, Autonomia:{self._autonomia}")

    matricula = property(getMatricula,setMatricula)
    velocidadeMaxima = property(getVelocidad,setVelocidad)
    autonomia = property(getAutonomia,setAutonomia)

    @abstractmethod
    def arrincar(self):
        pass

    def deter(self):
        print(f"O vehiculo {self._matricula} está detido")

    @abstractmethod
    def mostrardatos(self):
        pass
