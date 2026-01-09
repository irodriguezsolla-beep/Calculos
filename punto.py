class Punto:
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        if type(x)== int or type(x)== float:
            self.__x = x
        else:
            raise TypeError(f"La clase {type(x)} tiene que ser int o float")

    def getX(self):
        return self.__x


    def setY(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y
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
        p = Punto("2",1)
    except TypeError as t:
        print("Error: "+ str(t))
        x = float(input("Introduce el punto X: ")

        while type(x) == int or type(x) == float  :
            print("Punto no valido")
            x = input("Introduce el punto X: ")
        p  = Punto(x,1)
        print(p)
