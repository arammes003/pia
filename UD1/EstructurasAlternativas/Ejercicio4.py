# Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

# Funcion que pide la cantidad de euros
def pedirEuros():
    try:
        euros = int(input("Introduce una cantidad exacta de euros para hacer el desglose: "))
        return euros
    except ValueError:
        print("He dicho euros, no centimos ni otras cosas")
        return None

# Funcion que desglosa la cantidad de euros
# - Array con las opciones disponibles
# - Bucle que coge cada opcion del array
# - Calculamos cuantos opciones de ese billete/moneda darian una division exacta de la cantidad (es decir, que se puede dar cambio sin pasarte)
# - Restamos la cantidad total de dinero con laa opcion de ese billete/moneda y su cantidad
# - En cada ejecucion del bucle mostramos el desglose con la opcion de billete/moneda y su cantidad
def desglosarCantidad(cantidad):
    billetes = [500,  200, 100, 50, 20, 10, 5, 2, 1]

    for opcion in billetes:
        cambio = cantidad // opcion
        cantidad = cantidad - cambio * opcion

        if cambio > 0:
            print(f"{opcion}€: {cambio}")


# Funcion principal
def main():
    euros = pedirEuros()
    desglosarCantidad(euros)

main()