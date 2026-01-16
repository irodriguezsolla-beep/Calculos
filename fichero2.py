import pickle
import datetime

# Obtenemos la fecha y hora actual
fecha_hora = datetime.datetime.now()         # Llamamos a la función con ()

# Convertimos a string y separamos fecha y hora
data, hora = str(fecha_hora).split()         # data = '2026-01-16', hora = '14:23:45.123456'

# Ajustamos la hora para quitar microsegundos
hora = hora.split(".")[0]                     # '14:23:45'

# Separamos componentes de fecha y hora
amd = data.split("-")                         # ['2026', '01', '16']
hms = hora.split(":")                         # ['14', '23', '45']

# Creamos el diccionario
fecha_hora_dict = {
    "ano": amd[0],
    "mes": amd[1],
    "dia": amd[2],
    "hora": hms[0],
    "minuto": hms[1],
    "segundo": hms[2]
}

# Guardamos en un archivo binario usando pickle
with open("data.dat", "wb") as ficheiro: #write binary
    pickle.dump(fecha_hora_dict, ficheiro)

with open("data.dat", "rb") as ficheiro: #read binary
    dic = pickle.load(ficheiro)
    print(dic["hora"])
    print(dic["minuto"])

opcionUsuario = { "theme": "dark",
                  "font-size":14,
                  "show_line_number":True}

with open ("opcions.dat","wb") as fich:#guardar
    pickle.dump(opcionUsuario, fich)

with open ("opcions.dat","rb") as fich:# leer
    ops = pickle.load(fich)
    print(ops)
#pickle: dump y load