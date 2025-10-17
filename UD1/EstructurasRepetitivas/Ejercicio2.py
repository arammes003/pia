# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

# Funcion que pide la cantidad de numeros que van a iterar
def pedirCantidadNumeros():
    return int(input("Introduce una cantidad de numeros para iterar: "))

# Funcion que pide numeros
def pedirNumero(numIteraciones):
    cont = 0
    numeros = []
    while cont < numIteraciones:
        numeros.append(int(input("Introduce un numero: ")))
        cont += 1
    
    return numeros

# Funcion que analiza que valor tiene cada numero
def analizarNumeros(numeros):
    contMayores = 0
    contMenores = 0
    contIguales = 0

    for numero in numeros:
        if numero > 0:
            contMayores += 1
        elif numero < 0:
            contMenores += 1
        else:
            contIguales += 1

    return contMayores, contMenores, contIguales


# Funcion principal del ejercicio
#   1. Obtenemos la cantidad de numeros que vamos a iterar
#   2. Pedimos el listado de numeros
#   3. Analizamos los datos
#   4. Mostramos el mensaje
def main():
    vecesIterar = pedirCantidadNumeros()
    listadoNumeros = pedirNumero(vecesIterar)
    mayores, menores, iguales = analizarNumeros(listadoNumeros)
    print(f"Has introducido: {mayores} mayores a 0, {menores} menores a 0 y {iguales} iguales que 0")


# Llamada a la funcion principal
main()