def evaluar(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    if residuo == 0:
        respuesta = f"La división es exacta.\nCociente: {cociente}\nResiduo: {residuo}"
    else:
        respuesta = f"La división no es exacta.\nCociente: {cociente}\nResiduo: {residuo}"
    return respuesta

def main():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)

if __name__ == "__main__":
    main()