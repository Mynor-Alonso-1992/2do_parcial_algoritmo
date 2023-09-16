
##PLANTEAR Una candena en mayusculas o minusculas que retorne la cantidad de letras A o aa

def contar_letras_a(cadena):
   
    cadena = cadena.lower()
    contador = 0

    for letra in cadena:
        if letra == 'a':
            contador += 1

    return contador

# Solicitar la entrada del usuario
cadena = input("Ingrese una cadena de texto: ")

# Llama a la función para contar las letras "a" o "A"
cantidad_a = contar_letras_a(cadena)

# Imprime el resultado
print("La cantidad de letras 'a' o 'A' en la cadena es: {cantidad_a}")
