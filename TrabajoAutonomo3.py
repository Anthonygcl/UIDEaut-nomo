def determinar_ganador(jugador1, jugador2):
    """
    Determina el ganador basándose en las reglas de Piedra, Papel o Tijera.
    - Devuelve 'Empate' si ambos jugadores eligen lo mismo.
    - Devuelve 'Jugador 1 gana' o 'Jugador 2 gana' según las combinaciones ganadoras.
    """
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or \
         (jugador1 == "Papel" and jugador2 == "Piedra") or \
         (jugador1 == "Tijera" and jugador2 == "Papel"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def juego_piedra_papel_tijera():
    """
    Función principal para ejecutar el juego.
    """
    print("Bienvenidos a Piedra, Papel o Tijera")

    while True:
        # Entrada de los jugadores
        jugador1 = input("Jugador 1, elige Piedra, Papel o Tijera: ")
        jugador2 = input("Jugador 2, elige Piedra, Papel o Tijera: ")

        # Validación de entrada
        if jugador1 not in ["Piedra", "Papel", "Tijera"] or jugador2 not in ["Piedra", "Papel", "Tijera"]:
            print("Elección inválida. Asegúrate de escribir Piedra, Papel o Tijera correctamente.\n")
            continue  # Reinicia la ronda si la entrada no es válida

        # Determinar el ganador
        resultado = determinar_ganador(jugador1, jugador2)
        print(f"Resultado: {resultado}\n")

# Ejecutar el juego
juego_piedra_papel_tijera()
