from abc import ABC, abstractmethod
class Vehiculo(ABC):
    def __str__(self,matricula,velocidadeMaxima,autonomia):
        self.setMatricula(matricula)
        self.setVelocidad(velocidadeMaxima)
        self.setAutonimia(autonomia)

    def setMatricula(self,matricula):
         self.__matricula = matricula
    def getMatricula(self):
        return  self.__matricula

    def setVelocidad(self, velocidadeMaxima):
        self.__velocidadeMaxima = velocidadeMaxima
    def getVelocidad(self):
        return self.__velocidadeMaxima

    def setAutonomia(self,autonimia):
         self.__autonima = autonimia
    def getAutonomia(self):
        return  self.__autonomia

    def __str__(self):
        return (f"Matricula: {self.__matricula}, Velocidade:{self.__velocidadeMaxima}, Autonomia:{self.__autonima}")

    matricula = property(getMatricula,setMatricula)
    velocidadeMaxima = property(getVelocidad,setVelocidad)
    autonomia = property(getAutonomia,setAutonomia)

    @abstractmethod
    def arrincar(self):
        pass

    def deter(self):
        print(f"O vehiculo {self.__matricula} está detido")

    @abstractmethod
    def mostrardatos(self):
        pass
