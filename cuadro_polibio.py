# Cuadro de Polibio (sin Z, I y J separadas)

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXY"

# Crear matriz 5x5
matriz = []
indice = 0

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(alfabeto[indice])
        indice += 1
    matriz.append(fila)

# Mostrar matriz
print("Cuadro de Polibio:")
for fila in matriz:
    print(fila)


def cifrar(mensaje):
    mensaje = mensaje.upper()
    resultado = ""

    for letra in mensaje:
        if letra == " ":
            resultado += " "
            continue

        for i in range(5):
            for j in range(5):
                if matriz[i][j] == letra:
                    resultado += str(i+1) + str(j+1) + " "

    return resultado


def descifrar(codigo):
    pares = codigo.split()
    resultado = ""

    for par in pares:
        fila = int(par[0]) - 1
        columna = int(par[1]) - 1
        resultado += matriz[fila][columna]

    return resultado


# Menú
opcion = input("1. Cifrar\n2. Descifrar\nElige una opción: ")

if opcion == "1":
    mensaje = input("Mensaje a cifrar: ")
    cifrado = cifrar(mensaje)
    print("Mensaje cifrado:", cifrado)

elif opcion == "2":
    codigo = input("Código a descifrar: ")
    print("Mensaje descifrado:", descifrar(codigo))

else:
    print("Opción no válida")