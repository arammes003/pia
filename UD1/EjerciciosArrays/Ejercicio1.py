# 1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. 
# Carga las lista number con valores aleatorios entre 0 y 100. 
# En la lista square se deben almacenar los cuadrados de los valores que hay en number. 
# En la lista cube se deben almacenar los cubos de los valores que hay en number. 
# A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

import random
import pandas as pd

def define_list_number(cantity_numbers):
    number = []

    for _ in range(cantity_numbers):
        number.append(random.randint(0, 100))

    return number

def define_square_list(numbers):
    square_list = []

    for number in range(len(numbers)):
        square_number = numbers[number] ** 2
        square_list.append(square_number)

    return square_list

def define_cube_list(numbers):
    cube_list = []

    for number in range(len(numbers)):
        cube_number = numbers[number] ** 3
        cube_list.append(cube_number)

    return cube_list


def main():
    numbers = define_list_number(20)
    squares = define_square_list(numbers)
    cubes = define_cube_list(numbers)

    df = pd.DataFrame({
        'Number': numbers,
        'Square': squares,
        'Cube': cubes
    } , index=range(1, 21))

    print(df)


main()