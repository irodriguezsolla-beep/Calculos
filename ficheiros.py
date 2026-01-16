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

fichero = open("saudo.txt", "r")      # Abre el archivo saudo.txt en modo lectura
linha = fichero.readline()            # Lee la primera línea del archivo
while linha != "":                    # Mientras NO se llegue al final del archivo
    print(linha, end="")              # Muestra la línea por pantalla sin añadir otro salto
    linha = fichero.readline()        # Lee la siguiente línea
fichero.close()                       # Cierra el archivo
