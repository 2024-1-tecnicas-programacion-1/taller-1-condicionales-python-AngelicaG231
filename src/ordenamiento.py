def evaluar(numero1, numero2, numero3, numero4):
    # Usar sorted() para ordenar los números
    numeros = [numero1, numero2, numero3, numero4]
    numeros_ordenados = sorted(numeros)
    # Crear una cadena con los números ordenados
    return ' '.join(map(str, numeros_ordenados))

def main():
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    numero3 = int(input("Número 3: "))
    numero4 = int(input("Número 4: "))

    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)

if __name__ == "__main__":
    main()