class CalculadoraBinaria:
    def __init__(self, a, b):
        self.setA(a)
        self.setB(b)

    def setA(self, a):
        if type(a) == int:
            self.a = a
        else:
            raise ValueError("A debe ser un entero")

    def getA(self):
        return self.a

    def setB(self, b):
        if type(b) == int:
            self.b = b
        else:
            raise ValueError("B debe ser un entero")

    def getB(self):
        return self.b

    def operacion(self, op):
        match op:
            case "+":
                print(f"La suma es {self.a + self.b}")
            case "-":
                print(f"La resta es {self.a - self.b}")
            case "*":
                print(f"La multiplicación es {self.a * self.b}")
            case "/":
                if self.b != 0:
                    print(f"La división es {self.a / self.b}")
                else:
                    print("Error: división entre cero")
            case _:
                print("Operación no válida")

c = CalculadoraBinaria(2, 5)
c.operacion("+")
c.operacion("*")
