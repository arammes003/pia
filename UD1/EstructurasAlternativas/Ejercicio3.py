# Escribir un programa que lea un año indicar si es bisiesto (un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).

# Funcion que pide el año
def pedirAnio():
    return int(input("Introduce un año: "))

# Funcion que es bisiesto
#   1. Recibe el año
#   2. Devuelve si es o no bisiesto
def esBisiesto(anio):
    if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        return "Es bisiesto"
    else:
        return "No es bisiesto"
    
# Funcion principal
#   1. Obtiene año
#   2. Devuelve la salida
def main():
    print(esBisiesto(pedirAnio()))

# Llamada al programa
main()