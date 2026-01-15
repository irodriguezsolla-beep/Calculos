from DataError import DataError
class Data:
    def __init__(self,dia,mes,ano):
        self.setDia(dia)
        self.setMes(mes)
        self.setAno(ano)

    def setDia(self,dia):
        if type(dia) == int:
            if dia>= 1 or dia<=31:
                self.__dia = dia
            else:
                raise DataError(f"El número de dia estama solo puede estar entre 1 hasta 31")
        else:
            raise TypeError(f"El formato tiene que ser INT")
    def getDia(self):
        return self.__dia

    def getMes
        if type(mes) == int:
            if len(mes) == 2:
                if mes>=1 or mes<=12:
                    if mes = 1 or mes = 3 or mes = 5 or mes = 7 or mes = 8 or mes = 10 or mes = 12:

                    elif :

                else:
                    raise DataError(f"Los meses solo pueden ir desde 1 a 12")
            else:
                raise DataError(f"Los meses Los meses solo pueden ir desde 1 a 12")
        else:
            raise TypeError(f"El formato tiene que ser INT")