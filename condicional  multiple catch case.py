x = 30
match x:# se parece al if
    case 10:
        print("X é 10")
    case 20:
        print("X é 20")
    case _:
        print("X non é")

match x:
    case 10|20|30:
        print("X")
    case _:
        print("X...")
match x:
    case 10 if x % 2 ==0:
        print("X....")

l = (2,3,3)
match l:
    case( x,y):
        print(f"la posicion {x}, {y}")
    case (x,y,z):
        print(f"la pososicion es {x},{y} y {z} ")

persoa = {"nome":"Manuel","curso":"Dam"}

match persoa:
    case {"nome":nome,"curso":curso}:
        print(f"Nome:{nome},curso:{curso}")
    case _:
        print("Hostia")

class figura:
    pass
class Circulo(figura):
    def __init__(self,r):
        self.radio=r
class Rectangulo(figura):
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

f = Circulo(15)

match f:
    case Circulo( radio = r):
        print(f"A figura e un circulo de radio {r}")
    case Rectangulo(ancho,alto):
        print(f" a figura e un rectangulo con {ancho} de ancho y {alto} de alto")
