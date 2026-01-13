class persoa:
    def __init__(self,nome,dni,idade):
        self.setNome(nome)
        self.setDni(dni)
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
            if idade >=0:
                self.__idade = idade
            else:
                self.__idade = ("Error")
        else:
            self.__idade = ("Error")
    def getIdade(self):
        return self.__idade

    def setDni(self,dni):
        if type(dni) == str:
            if len(dni) == 9 and dni[:-1].isdigit() and dni[:-1].isalpha():
                letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                resto = int(dni[:-1])%23
                if letraDni[resto] == dni[-1:].upper():
                    return True
                else:
                    return False
            else:
                raise ValueError(f"El numero de carateres no es el adecuado")
        else:
            raise TypeError(f"el tipo de {type(dni)} tiene que ser str")
    def getDni(self):
        return self.__dni

    nome = property(getNome,setNome)
    idade = property(getIdade,setIdade)
    dni = property(getDni,setDni)

    def __str__(self):
        return self.__nome + " " + str(self.__dni) + " " + str(self.__idade)

if __name__=='__main__':
