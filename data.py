class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

        if not self.es_fecha_valida():
            raise ValueError("Fecha no válida")

    def es_bisiesto(self):
        return (self.anio % 4 == 0 and self.anio % 100 != 0) or (self.anio % 400 == 0)

    def dias_del_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            return 29 if self.es_bisiesto() else 28
        else:
            return 0

    def es_fecha_valida(self):
        if self.anio < 1:
            return False
        if self.mes < 1 or self.mes > 12:
            return False
        if self.dia < 1 or self.dia > self.dias_del_mes():
            return False
        return True

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"
