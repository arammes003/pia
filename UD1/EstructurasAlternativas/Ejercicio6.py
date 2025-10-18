# Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().

# Funcion que pide los numeros
# - Creamos un array donde se almacenan los numeros
# - Bucle que se ejecuta 3 veces (1, num que empieza) (4, donde acaba por que no se tiene en cuenta el numero del limite superior)
# - Pedimos el numero
# - Guardamos el numero en el array
# - Devolvemos el array
def pedirNumeros():
    numeros = []

    for i in range(1, 4):
        num = int(input(f"Introduce el numero {i}: "))
        numeros.append(num)
    
    return numeros

# Funcion que obtiene el mayor numero sin usar max()
#   - Usamos el metodo sorted
#   - Le pasamos los numeros
#   - Reverse=true para que ordene de mayor a menor
#   - [0] para que devuelva la primera posicion (el mayor)
def obtenerMayor(numeros):
    return sorted(numeros, reverse=True)[0]

# Funcion principal
#   1. Pedimos todos los numeros
#   2. Llamamos a la funcion que obtiene el mayor
#   3. Imprimimos un mensaje con el mayor
def main():
    numeros = pedirNumeros()
    mayor = obtenerMayor(numeros)

    print(f"El mayor numero introducido es: {mayor}")


# Llamada a la funcion main
main()