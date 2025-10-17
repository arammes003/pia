# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 

# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

# Funcion que pide los limites del intervalo
def pedirIntervalos():
    intervaloInferior = int(input("Introduce el valor del limite inferior: "))
    intervaloSuperior = int(input("Introduce el valor del limite superior: "))

    if intervaloSuperior < intervaloInferior:
        while intervaloSuperior < intervaloInferior:
            intervaloSuperior = int(input("Venga crack ahora que sea superior de verdad: "))

    return intervaloInferior, intervaloSuperior

# Funcion que pide numeros
def introducirNumeros():
    numeros = []
    num = int(input("Introduce un numero (0 si quieres terminá): "))

    while num != 0:
        numeros.append(num)
        num = int(input("Introduce un numero (0 si quieres terminá): "))

    print("Terminao por pulsar el 0")
    return numeros

# Funcion que suma los valores que estan en el intervalo
def sumarNumerosIntervalo(valorInferior, valorSuperior, numeros):
    suma = 0

    for num in numeros:
        if valorInferior <= num <= valorSuperior:
            suma += num

    return suma

# Funcion que obtiene los numeros que estan fuera del intervalo
def fueraIntervalo(valorInferior, valorSuperior, numeros):
    fuera = []

    for num in numeros:
        if num < valorInferior or num > valorSuperior:
            fuera.append(num)
    
    return len(fuera)

# Funcion que obtiene si hay algun numero igual a los limites del intervalo
def valorIgualLimite(valorInferior, valorSuperior, numeros):
    iguales = False

    for num in numeros:
        if valorInferior == num or num == valorSuperior:
            iguales = True
    
    return iguales

# Funcion principal
#   1. Pide los valores de los intervalos
#   2. Pide los numeros y los guarda
#   3. Obtiene la suma de los valores que estan dentro del intervalo 
#   4. Obtiene la cantidad de numeros que estan fuera del intervalo
#   5. Informa si se ha introducido algun numero que sea igual a algun valor del limite
def main():
    valorInferior, valorSuperior = pedirIntervalos()
    numerosIntroducidos = introducirNumeros()

    print(f"La suma de los numeros que estan en el intervalo es de: {sumarNumerosIntervalo(valorInferior, valorSuperior, numerosIntroducidos)}")

    print(f"Los numeros que estan fuera del intervalo son {fueraIntervalo(valorInferior, valorSuperior, numerosIntroducidos)}")

    if valorIgualLimite(valorInferior, valorSuperior, numerosIntroducidos):
        print(f"Se ha introducido algun numero igual a un limite")
    else:
        print(f"No se ha introducido algun numero igual a un limite")

# Llamada al ejercicio
main()
