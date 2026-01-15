from Persoa2 import persoa
from ErrorDNi import DniError
from ErrorLicencia import LicenciaError
class Persona(persoa):
    def __init__(self,nome,dni,idade,direcion):
        super().__init__(nome,dni,idade)
        self.setDirecion(direcion)

    def setDirecion(self,direcion):
        self.direcion = direcion
    def getDirecion(self):
        return self.direcion

    def __str__(self):
        return (f"El nombre es {self.getNome()}, o DNI es: {self.getDni()} , la edad es: {self.getIdade()} y la direción es: {self.getDirecion()}")

class Deportista:
    def __init__(self,deporte,club,licencia):
        self.setDeporte(deporte)
        self.setClub(club)
        self.setLicencia(licencia)

    def setDeporte(self,deporte):
        if type(deporte) == str:
            self.__deporte = deporte
        else:
            raise TypeError(f"El formato no es el corecto")
    def getDeporte(self):
        return self.__deporte

    def setClub(self,club):
        if type(club)== str:
            self.__club = club
        else:
            raise TypeError(f"El formato no es el corecto")
    def getClub(self):
        return self.__club

    def setLicencia(self,licencia):
        if type(licencia) == str:
            if len(licencia) == 13:
                if licencia[:4].isdigit() and licencia[:4] == "2026":
                    if licencia[4:7].isalpha() and licencia[4:7].upper() == self.getDeporte()[:3].upper():
                        if licencia[-6:].isdigit():
                            self.__licencia = licencia
                        else:
                            raise LicenciaError (f"Los ultimos 6 digitos tiene que ser números")
                    else:
                        raise LicenciaError (f"Los digitos de de deporte no son correctos ")
                else:
                    raise LicenciaError (f"O los 4 pimeros dijitos o no son 2026 o no son números")
            else:
                raise LicenciaError (f"La cantidad de caractere no es la adecuada tiene que ser 13 caracteres")
        else:
            raise TypeError(f"El formato no es el corecto")
    def getLicencia(self):
        return self.__licencia
    def __str__(self):
        return (f"El deporte que hace es: {self.getDeporte()}, pertenecer al club: {self.getClub()}, y su licencia es. {self.getLicencia()}")
if __name__=='__main__':
    try:
        alan = Persona("Alan","00000000T",20,"Gondomar")
        print("DNI válido:",alan)
    except DniError as e:
        print("Error con p1: ",e)

    try:
        De = Deportista("Futbal","Real Madrid","2026Fut300000")
        print("Licencia: ", De)
    except TypeError as t:
        print(t)
    except LicenciaError as l:
        print(l)
