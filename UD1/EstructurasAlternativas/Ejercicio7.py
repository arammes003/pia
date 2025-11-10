# Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max()..

# Funcion que pide los numeros
# - Creamos un array donde se almacenan los numeros
# - Bucle que se ejecuta 5 veces (1, num que empieza) (6, donde acaba por que no se tiene en cuenta el numero del limite superior)
# - Pedimos el numero
# - Guardamos el numero en el array
# - Devolvemos el array
def pedir_numeros():
    num1 = int(input("Introduce el valor del primer numero: "))
    num2 = int(input("Introduce el valor del segundo numero: "))
    num3 = int(input("Introduce el valor del tercer numero: "))
    num4 = int(input("Introduce el valor del cuarto numero: "))
    num5 = int(input("Introduce el valor del quinto numero: "))

    return num1, num2, num3, num4, num5

# Funcion que obtiene el mayor numero sin usar max()
#   - Usamos el metodo sorted
#   - Le pasamos los numeros
#   - Reverse=true para que ordene de mayor a menor
#   - [0] para que devuelva la primera posicion (el mayor)
def obtenerMayor(num1, num2, num3, num4, num5):
    mayor = num1

    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    if num4 > mayor:
        mayor = num4
    if num5 > mayor:
        mayor = num5

    return mayor

# Funcion principal
#   1. Pedimos todos los numeros
#   2. Llamamos a la funcion que obtiene el mayor
#   3. Imprimimos un mensaje con el mayor
def main():
    n1, n2, n3, n4, n5 = pedir_numeros()
    mayor = obtenerMayor(n1, n2, n3, n4, n5)

    print(f"El mayor número introducido es: {mayor}")


# Llamada a la funcion main
main()