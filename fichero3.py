import csv

with open("exemplo.csv","r")as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow("Nome","Edade","Xenero")
    writer.writerow("Pedro", "23", "Home")
    writer.writerow("Rosa", "25", "Muller")