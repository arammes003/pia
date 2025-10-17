# Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

# Funcion que compara las edades
#   1. Recibe las edades
#   2. Comprueba cual es mayor
#   3. Si son iguales avisa al usuario.
def compararEdades(edad1, edad2):
    if (edad1 > edad2): 
        print(f"La persona 1 tiene {edad1} y es mayor que la persona 2 que tiene: {edad2}")
    elif (edad2 > edad1):
        print(f"La persona 2 tiene {edad2} y es mayor que la persona 1 que tiene: {edad1}")
    else:
        print(f"Ambas personas tienen {edad1} años")

# Funcion principal que:
#   1. Solicita edades
#   2. Comprueba que sean edades validas
#   3. Llama a la funcion que compara las edades
def main():
    edad1 = int(input("Introduce la edad de la persona 1: "))
    edad2 = int(input("Introduce la edad de la persona 2: "))

    if (edad1 < 0 or edad2 < 0):
        print("No sabia que se podian tener años negativos")
        return
    
    if edad1 > 110 or edad2 > 110:
        print("Vale que sea mayor pero tanto no se rick, parece falso...")
        return

    compararEdades(edad1, edad2)

# Llamada al programa
main()