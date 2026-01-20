import csv

with open("exemplo.csv","w")as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow("Nome","Edade","Xenero")
    writer.writerow("Pedro", "23", "Home")
    writer.writerow("Rosa", "25", "Muller")

with open("exemplo2.csv","w")as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow("Nome"+","+"Edade"+","+"Xenero"+","+"\n")
    writer.writerow("Pedro"+","+"23"+","+"Home"+","+"\n")
    writer.writerow("Rosa"+","+"25"+","+"Muller")

with open ("exemplo.csv", "r") as ficheiro:
    reader = csv.reader(ficheiroro)
    for fila in reader:
        print(fila)