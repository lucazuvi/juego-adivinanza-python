import random


def juegoAdivinanza():
    numeroRandom = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanzas!")
    print("Intenta adivinar el numero entre el 1 y el 100")

    while not adivinado:
        adivinanza = input("Prueba un numero: ")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numeroRandom:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numeroRandom:
                print(f"El numer secreto es menor a {adivinanza}")
            else:
                print(f"Felcidades! El numero secreto es el {adivinanza}")
                print(f"Numero total de intentos: {intentos}")
                adivinado = True

        else:
            print("Por favor, ingrese un digito del 1 al 100")


juegoAdivinanza()
