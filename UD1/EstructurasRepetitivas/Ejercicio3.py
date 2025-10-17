# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

# Libreria que permite generar numeros aleatorios
import random

# Funcion que genera un numero aleatorio
def generarNumeroRandom():
    return random.randint(1, 100)

# Funcion que pide numeros
def pedirNumero():
    return int(input("Introduce un numero: "))


# Funcion que compara los numeros
# - Compara el numero introducido con el elegido
# - Avisa si es mayor o menor
# - Avisa de los intentos restantes
# - Avisa cuando aciertas
# - Avisa en cuantos intentos has acertado
def compararNumeros(numRandom):
    numIntentos = 10
    intentoActual = 0

    while numIntentos >= 0:
        numIntroducido = pedirNumero()

        if numIntroducido > numRandom:
            print("El numero introducido es mayor que el elegido.")
        elif numIntroducido < numRandom:
            print("El numero introducido es menor que el elegido.")
        elif numIntroducido == numRandom:
            print("ACERTASTE!!!")
            print(f"Lo has acertado en {intentoActual} intentos")
            return
        
        numIntentos -= 1
        intentoActual += 1
        print(f"Te quedan {numIntentos} intentos")

    print(f"Se acabaron los intentos. El numero elegido era {numRandom}")



# Funcion principal
def main():
    print("Tienes 10 intentos para adivinar el numero.")
    compararNumeros(generarNumeroRandom())


# Llamada al ejercicio
main()
