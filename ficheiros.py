import datetime

try:
    ficheiro = open("/home/dam/Documentos/saudo.txt", "r")
    for linha in ficheiro:
        print(linha)
    ficheiro.close()
except FileNotFoundError as e:
    print("Erro ao abrir o ficheiro:", e)

# Fecha y hora actual
data_hora = datetime.datetime.now()
data, hora = str(data_hora).split()

# Escritura
ficheiro = open("Editorial.txt", "w")
ficheiro.write("Ola, son Isaac\n")
ficheiro.write(data + "\n")
ficheiro.write(hora + "\n")
ficheiro.write("Remato e pecho o ficheiro\n")
ficheiro.close()

# Lectura
ficheiro = open("Editorial.txt", "r")
lectura = ficheiro.read()
print(lectura)
ficheiro.close()

fichero = open("saudo.txt","r")
linha = fichero.readline()
    while linha != None:
        print(linha)
        linha = fichero.readline()
        ficheiro.close()