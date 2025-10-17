# Crea un programa que pida un número por teclado al usuario y diga si es primo. En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.

# Funcion que pide un numero
def pedirNumero():
    try: 
        return int(input("Introduce un numero para saber si es primo o no: "))
    except ValueError:
        return None

# Funcion que comprueba que sea un numero primo
def esPrimo(entrada):    
    if entrada is None:
        return print("Si introduces un numero sabremos si es primo o no...")

    if entrada < 2:
        return print("Introduce un numero mayor a 2 para ejecutar.")

    for i in range(2, entrada):
        if (entrada % i) == 0:
            return print(f"El numero {entrada} no es primo")
        else:
            return print(f"El numero {entrada} es primo")
    

# Funcion principal
#   1. Pedimos el numero
#   2. Comprobamos que sea primo
def main():
    numero = pedirNumero()
    esPrimo(numero)

# Llamada al ejercicio
main()