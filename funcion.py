#asignacion funcion a variable

def suma(a,b):
    return a + b
def saudo():
    print("Ola")

adicion = suma
print(adicion(1,2))


benvida = saudo
print(benvida)

#asignacion funcion argumento
def executa(f,v1,v2):
    return f(v1,v2)

resultado= executa(suma,2,2)
print(resultado)

def multiplicacion(y):
    def producto (x):
        return x * y
    return producto

dobre = multiplicacion(2)
# dobre pasa a ser def producto
print(dobre(5))


#decoradores
def decorador(func):
    def envoltorio():
        print("Executa antes da funcion", func.__name__)
        func()
        print("Se executa despois de funtio", func.__name__)
    return envoltorio

@decorador
def saudo2():
    print("ola2")
funcionDecorativa = decorador(saudo)

funcionDecorativa()
decorador(saudo)

print(funcionDecorativa)