"""Juego de adivinar un número aleatorio entre 1 y 100.

El usuario dispone de un máximo de diez intentos por partida.
El programa ofrece pistas y mantiene un registro de las partidas
jugadas y ganadas.

Módulo: Programación · UD 3
Autor: Jose María Mas Chicharro y Andrea Mira Hernández
Fecha: 18/11/2026
"""

from random import randint


def pedir_numero():
    """Pide y devuelve un número entero válido entre 1 y 100."""
    while True:
        try:
            numero = int(input("Introduce un número entre 1 y 100: "))

            if 1 <= numero <= 100:
                return numero

            print("Error: el número debe estar entre 1 y 100.")

        except ValueError:
            print("Error: debes introducir un número entero.")


def jugar_partida():
    """Realiza una partida y devuelve si se ha ganado y los intentos usados."""
    numero_secreto = randint(1, 100)
    intentos = 0

    print("\n--- NUEVA PARTIDA ---")
    print("Tienes un máximo de 10 intentos.")

    while intentos < 10:
        numero = pedir_numero()
        intentos += 1

        if numero == numero_secreto:
            print(f"¡Has acertado en {intentos} intentos!")
            return True, intentos

        elif numero < numero_secreto:
            print("El número buscado es mayor.")

        else:
            print("El número buscado es menor.")

        print("Intentos restantes:", 10 - intentos)

    print("\nHas agotado los 10 intentos.")
    print("El número correcto era:", numero_secreto)

    return False, intentos


def preguntar_repetir():
    """Pregunta si el usuario quiere jugar otra partida."""
    while True:
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

        if respuesta == "s":
            return True

        elif respuesta == "n":
            return False

        else:
            print("Respuesta no válida. Introduce 's' o 'n'.")


def main():
    """Controla las partidas y muestra las estadísticas del juego."""
    partidas_jugadas = 0
    partidas_ganadas = 0

    while True:
        partidas_jugadas += 1

        ganada, intentos = jugar_partida()

        if ganada:
            partidas_ganadas += 1

        print("\n--- ESTADÍSTICAS ---")
        print("Partidas jugadas:", partidas_jugadas)
        print("Partidas ganadas:", partidas_ganadas)

        if not preguntar_repetir():
            break

    print("\n--- ESTADÍSTICAS FINALES ---")
    print("Partidas jugadas:", partidas_jugadas)
    print("Partidas ganadas:", partidas_ganadas)
    print("Gracias por jugar.")


if __name__ == "__main__":
    main()