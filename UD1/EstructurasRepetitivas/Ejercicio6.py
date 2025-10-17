# Crea un programa que muestre en pantalla los N primeros número primos. El valor de N se pide por teclado al usuario/a.

# Funcion que pide la cantidad de numeros que quiere sacar
def obtenerCantidadNumeros():
    return int(input("Introduce cuantos numeros primos quieres sacar: "))

# Funcion que obtiene los numeros primos
# - Declaramos array para guardar los primos
# - Creamos una variable cont que seran los numeros de cada iteracion
# - Bucle mientras que la cantidad de la variable numeros primos sea menor a la cantidad
# - Contador = 2 porquie el 1 no es primo y lo devolveria como primo
# - Bucle for que hace la raiz cuadrada de cont y suma 1 porque range no incluye el limite superior
def obtenerPrimos(cantidad):
    numerosPrimos = []

    cont = 2
    while len(numerosPrimos) < cantidad:
        esPrimo = True

        for i in range(2, int(cont ** 0.5) + 1):
            if cont % i == 0:
                esPrimo = False
                break

        if esPrimo:
            numerosPrimos.append(cont)
        
        cont += 1
    
    return print(numerosPrimos)    
    
# Funcion main
def main():
    cantidadNumeros = obtenerCantidadNumeros()
    obtenerPrimos(cantidadNumeros)

## Llamada al ejercicio
main()