def descifrar_cesar(texto, desplazamiento):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ""
    
    for letra in texto:
        if letra.lower() in alfabeto:
            es_mayuscula = letra.isupper()
            indice = alfabeto.index(letra.lower())
            
            # Movimiento hacia atrás para descifrar
            nuevo_indice = (indice + desplazamiento) % len(alfabeto)
            nueva_letra = alfabeto[nuevo_indice]
            
            if es_mayuscula:
                nueva_letra = nueva_letra.upper()
                
            resultado += nueva_letra
        else:
            # Mantener espacios y signos
            resultado += letra
    
    return resultado


# -------- PROGRAMA PRINCIPAL --------

texto_cifrado = input("Ingresa el texto cifrado: ")

print("\nPosibles descifrados:\n")

for i in range(27):  # 27 letras en el alfabeto español
    print(f"Desplazamiento {i}: {descifrar_cesar(texto_cifrado, i)}")