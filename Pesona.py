class persoa:
    def __init__(self,nome,dni,idade):
        self.setNome(nome)
        self.__dni = dni
        self.setIdade(idade)

    def setNome(self,nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            self.__nome = ("Error")
    def getNome(self):
        return self.__nome

    def setIdade(self,idade):
        if type(idade) == int:
            self.__idade = idade
        else:
            self.__idade = ("Error")
    def getIdade(self):
        return self.__idade

    def __str__(self):
        return self.__nome + " " + str(self.__dni) + " " + str(self.__idade)
if __name__=='__main__':
    p = persoa("Alan",554380238,t)
    try:
        print(p)
    except ValueError:
        print("Se tiene que poner un numero entero")
        intentos = 0

        i = int(input("Introduce un número la edada: "))

        while i == 0 and intentos < 2:
            intentos += 1
            i = int(input("Introduce un número la edada: "))
        p.idade = i

        print(p)
    finally:
        print("Fin del programa")