from datetime import datetime

def evaluar(dia, mes, año):
    fecha_nacimiento = datetime(año, mes, dia)
    fecha_actual = datetime.now()
    edad_usuario = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return f"Usted tiene {edad_usuario} años de edad"

if __name__ == "__main__":
    print("Ingrese su fecha de nacimiento.")
    dia = int(input("Día:"))
    mes = int(input("Mes:"))
    año = int(input("Año:"))

    respuesta = evaluar(dia, mes, año)
    print(respuesta)
