import os
from time import sleep

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola dependiendo del sistema operativo.
    - Para Windows usa 'cls'.
    - Para otros sistemas (Linux/Mac), usa 'clear'.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def determinar_ganador(jugador1, jugador2):
    """
    Determina el ganador basándose en las reglas de Piedra, Papel o Tijera.
    - Devuelve 'Empate' si ambos jugadores eligen lo mismo.
    - Devuelve 'Jugador 1 gana' o 'Jugador 2 gana' según las combinaciones ganadoras.
    """
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or\
         (jugador1 == "Papel" and jugador2 == "Piedra") or\
         (jugador1 == "Tijera" and jugador2 == "Papel"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def juego_piedra_papel_tijera():
    """
    Función principal para ejecutar el juego.
    - Incluye un bucle para jugar múltiples rondas.
    - Permite a los jugadores repetir el juego o terminarlo.
    """
    print("Bienvenidos a Piedra, Papel o Tijera")

    while True:
        # Entrada del Jugador 1
        jugador1 = input("Jugador 1, elige Piedra, Papel o Tijera: ").title()
        limpiar_pantalla()  # Limpia la pantalla para ocultar la elección del Jugador 1
        print("\n" * 5)  # Espacio adicional para ocultar la selección
        print("El Jugador 1 ya realizó su elección")
        sleep(2)  # Pausa para permitir que el Jugador 2 espere su turno
        limpiar_pantalla()

        # Entrada del Jugador 2
        jugador2 = input("Jugador 2, elige Piedra, Papel o Tijera: ").title()
        limpiar_pantalla()

        # Validación de entrada
        if jugador1 not in ["Piedra", "Papel", "Tijera"] or jugador2 not in ["Piedra", "Papel", "Tijera"]:
            print("Elección inválida. Asegúrate de escribir Piedra, Papel o Tijera correctamente.")
            continue  # Reinicia la ronda si la entrada no es válida

        # Determinar el ganador
        resultado = determinar_ganador(jugador1, jugador2)
        print(f"Resultado: {resultado}")

        # Preguntar si quieren jugar otra ronda
        jugar_otra = input("¿Quieres jugar otra ronda? (si/no): ").lower()
        if jugar_otra != "si":
            print("Gracias por jugar, hasta la próxima.")
            break  # Sale del bucle principal y termina el juego

# Ejecutar el juego
juego_piedra_papel_tijera()
