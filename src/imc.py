def evaluar(peso, estatura, edad):
    condicion = ""
    imc = peso / (estatura * estatura)

    if edad < 45:
        if edad < 22:
            condicion = "bajo"
        elif 22 <= edad and imc >= 22 and imc < 27:
            condicion = "medio"
        else:
            condicion = "alto"
    else:
        if edad < 22:
            condicion = "medio"
        elif 22 <= edad and imc >= 22 and imc < 27:
            condicion = "alto"
        else:
            condicion = "muy alto"
    return condicion

def main():
    peso = float(input("Ingresar tu peso: "))
    estatura = float(input("Ingresa tu estatura estatura: "))
    edad = int(input("Ingresa tu edad: "))

    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)

if __name__ == "__main__":
    main()