def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or \
         (jugador1 == "Papel" and jugador2 == "Piedra") or \
         (jugador1 == "Tijera" and jugador2 == "Papel"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def juego_piedra_papel_tijera():
    print("Bienvenidos al juego de Piedra, Papel o Tijera")
    jugador1 = input("Jugador 1, elige Piedra, Papel o Tijera: ")
    jugador2 = input("Jugador 2, elige Piedra, Papel o Tijera: ")
juego_piedra_papel_tijera()
jugador1 = input("Jugador 1, elige Piedra, Papel o Tijera: ")
