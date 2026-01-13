class Punto:
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        if type(x)== int or type(x)== float:
            if x>=0:
                self.__x = x
            else:
                raise ValueError(f"O valor de x ={x} no pertenece a primer cuadrante")
        else:
            raise TypeError(f"La clase {type(x)} tiene que ser int o float")

    def getX(self):
        return self.__x


    def setY(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError(f"O valor de y ={y} no pertenece a primer cuadrante")
        else:
            raise TypeError(f"La clase {type(y)} tiene que ser int o float")
    def getY(self):
        return self.__y
    y = property(getY,setY)
    x = property(getX,setX)

    def __str__(self):
        return f"El punto es {self.__x} x , {self.__y} "

if __name__=='__main__':
    try:
        p = Punto(3,1)
    except TypeError as t:
        print("Error: "+ str(t))

    except ValueError as e:
        print("Error: " + str(e))

    print(p)