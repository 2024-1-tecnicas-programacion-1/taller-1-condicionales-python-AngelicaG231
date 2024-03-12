def evaluar(numero1, numero2, numero3, numero4):
    # Usaré el algoritmo de ordenamiento burbuja
    numeros = [numero1, numero2, numero3, numero4]
    nu = len(numeros)
    for i in range(nu - 1):
        for j in range(nu - i - 1):
            if numeros[j] > numeros[j + 1]:
                temp = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temp
    # Crear una cadena sin modificar un número
    return ' '.join(map(str, numeros))

def main():
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    numero3 = int(input("Número 3: "))
    numero4 = int(input("Número 4: "))

    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)