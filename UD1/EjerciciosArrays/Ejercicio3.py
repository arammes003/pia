# 3. Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

import numpy as np

def define_numbers(cantity_numbers):
    return np.random.randint(0, 100, cantity_numbers)

def main():
    numbers = define_numbers(20)
    
    pares = numbers[numbers % 2 == 0]
    impares = numbers[numbers % 2 != 0]

    numeros_ordenados = np.concatenate((pares, impares))
            
    print(numeros_ordenados)

main()