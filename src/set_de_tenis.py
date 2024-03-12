def evaluar(numVictoriasA, numVictoriasB):
    # Verificar si el resultado es inválido
    if numVictoriasA < 0 or numVictoriasB < 0 or abs(numVictoriasA - numVictoriasB) > 2:
        return "Resultado inválido"

    # Verificar término de set
    if numVictoriasA >= 6 and numVictoriasB >= 6:
        if abs(numVictoriasA - numVictoriasB) >= 2:
            return "El jugador A ganó el set" if numVictoriasA > numVictoriasB else "El jugador B ganó el set"
        else:
            return "El set aún no ha terminado"

    # Verificar set no terminado
    if numVictoriasA == 6 and numVictoriasB < 5:
        return "El set aún no ha terminado"
    if numVictoriasB == 6 and numVictoriasA < 5:
        return "El set aún no ha terminado"

    # El set ha terminado y ninguno de los jugadores tiene más de 6 juegos
    return "El jugador A ganó el set" if numVictoriasA > numVictoriasB else "El jugador B ganó el set" if numVictoriasB > numVictoriasA else "El set está empatado"

if __name__ == "__main__":
    numVictoriasA = int(input("Los juegos ganados por A: "))
    numVictoriasB = int(input("Los juegos ganados por B: "))

    respuesta = evaluar(numVictoriasA, numVictoriasB)
    print(respuesta)
