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

ficheiro = open("saudo.txt", "r")        # Abrimos el archivo en modo lectura
lectura = ficheiro.readlines()           # Leemos **todas las líneas** y las guardamos en una lista
print(lectura)                           # Mostramos la lista en pantalla
ficheiro.close()                         # Cerramos el archivo

with open("saudo.txt", "r") as ficheiro: # Abrimos el archivo en modo lectura usando 'with' (se cierra automáticamente)
   l = 0                                 # Inicializamos un contador de líneas
   for linha in ficheiro:                # Recorremos línea por línea
       l += 1                            # Sumamos 1 por cada línea
   print(f"O ficheiro tem {l} linhas")  # Mostramos el total de líneas

