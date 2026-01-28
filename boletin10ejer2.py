from DataError import DataError
class Data:
    def __init__(self,dia,mes,ano):
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)



    def setDia(self,dia):
        if type(dia) == int:
            if dia>= 1 or dia<=31:
                self.__dia = dia
            else:
                raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
        else:
            raise TypeError(f"El formato tiene que ser INT")
    def getDia(self):
        return self.__dia

    def setMes(self,mes):
        if type(mes) == int:
            if len(mes) == 2:
                if mes>=1 or mes<=12:
                    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                        if self.__dia>= 1 or dia<=31:
                            self.__mes = mes
                        else:
                            raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
                    elif mmes == 4 or mes == 6 or mes ==9 or mes == 11:
                        if dia>= 1 or dia<=30:
                            self.__mes = mes
                        else:
                            raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
                    elif mes == 2:
                        if dia >= 1 or dia <= 29:
                            self.__mes = mes
                        else:
                            raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
                else:
                    raise DataError(f"Los meses solo pueden ir desde 1 a 12")
            else:
                raise DataError(f"Los meses Los meses solo pueden ir desde 1 a 12")
        else:
            raise TypeError(f"El formato tiene que ser INT")
    def getMes(self):
        return self.__mes

    def __str__(self):
        return print(f"Dia: {self.__dia}, Mes: {self.__mes}")

if __name__=='__main__':
    D = Data(31,6)
    try:

    except DataError as e:
        print("Error con p1: ",e)
