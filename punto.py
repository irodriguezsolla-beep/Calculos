from abc import ABC, abstractmethod
class Punto(ABC):
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        if type(x)== int or type(x)== float:
            if x>=0:
                self._x = x
            else:
                raise ValueError(f"O valor de x ={x} no pertenece a primer cuadrante")
        else:
            raise TypeError(f"La clase {type(x)} tiene que ser int o float")

    def getX(self):
        return self._x


    def setY(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self._y = y
            else:
                raise ValueError(f"O valor de y ={y} no pertenece a primer cuadrante")
        else:
            raise TypeError(f"La clase {type(y)} tiene que ser int o float")
    def getY(self):
        return self._y
    y = property(getY,setY)
    x = property(getX,setX)

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularVolumen(self):
        pass

    def __str__(self):
        return f"El punto es {self._x} x , {self._y} "

if __name__=='__main__':
    try:
        p = Punto(3,1)
    except TypeError as t:
        print("Error: "+ str(t))

    except ValueError as e:
        print("Error: " + str(e))

    print(p)
