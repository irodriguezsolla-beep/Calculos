import csv
import json

datos = {"nome": "Jose", "edad": 30, "xenero": "Home"}

# Guardar JSON
with open("ejemplo.json", "w") as fichero:
    json.dump(datos, fichero)

# Leer JSON
with open("ejemplo.json", "r") as fichero:
    datoJson = json.load(fichero)
    print(datoJson)
    print(type(datoJson))

# Guardar en CSV
with open("ejemplo.csv", "a", newline="") as fichero:
    writer = csv.writer(fichero)
    writer.writerow(datoJson.keys())
    writer.writerow(datoJson.values())
