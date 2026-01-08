class calculadora:
    def __init__(self,a,b):
        self.set_a(a)
        self.set_b(b)

    def set_a(self,a):
        if isinstance(a, int) or isinstance(a, float):
            self.__a = a
        else:
            self.__a = 0
    def get_a(self):
        return self.__a

    def set_b(self,b):
        if isinstance(b, int) or isinstance(b, float):
            self.__b = b
        else:
            self.__b = 0
    def get_b(self):
        return self.__b

    def calcular(self,op):
        if op == "+":
            return self.__a + self.__b
        if op == "-":
            return self.__a - self.__b
        if op == "*":
            return self.__a * self.__b
        if op == "/":
            return self.__a / self.__b

    a = property(get_a,set_a)
    b = property(get_b,set_b)

if __name__=='__main__':
    c1 = calculadora(14,15)
    print(c1.calcular("/"))
    c2 = calculadora(2,0)
    print(c2.calcular("/"))

    try:#escepción
        print(c2.calcular("/"))
    except ZeroDivisionError:
        print("No se pode dividir por cero")