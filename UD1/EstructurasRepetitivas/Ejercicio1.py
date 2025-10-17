# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Funcion que pide los numeros
# - Devuelve los dos numeros
def pedirNumeros():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    return num1, num2

# Funcion que obtiene los pares entre dos numeros
def obtenerPares(num1, num2):
    while num1 < num2:
        if num1 % 2 == 0:
            print(num1)
        num1 += 1

# Funcion principal del proyecto
#   1. Mensaje informativo del ejercicio
#   2. Pedimos los numeros
#   3. Llamamos a la funcion que obtiene los pares
def main():
    print("----------PARES ENTRE DOS NUMEROS-----------")
    num1, num2 = pedirNumeros()
    obtenerPares(num1, num2)

# Ejecucion del ejercicio
main()