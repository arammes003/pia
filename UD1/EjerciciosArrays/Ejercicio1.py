"""
    Program: Generate 3 list of 20 int numbers, with names number, square and cube.
    Description:
    Author: Alfonso Ramírez Mestanza
    Date: 05/11/2025
"""

# 1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube.
# Carga las lista number con valores aleatorios entre 0 y 100. 
# En la lista square se deben almacenar los cuadrados de los valores que hay en number. 
# En la lista cube se deben almacenar los cubos de los valores que hay en number. 
# A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

import random
import pandas as pd

MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 100
NUMBERS_COUNT = 20
START_COLUMN_NUMBER = 1
END_COLUMN_NUMBER = 20 + 1


def generate_numbers(numbers_count):
    numbers = []

    for _ in range(numbers_count):
        numbers.append(random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER))

    return numbers

def generate_square_numbers(numbers):
    square_list = []

    for number in range(len(numbers)):
        square_number = numbers[number] ** 2
        square_list.append(square_number)

    return square_list

def generate_cube_numbers(numbers):
    cube_list = []

    for number in range(len(numbers)):
        cube_number = numbers[number] ** 3
        cube_list.append(cube_number)

    return cube_list


def main():
    numbers = generate_numbers(NUMBERS_COUNT)
    squares = generate_square_numbers(numbers)
    cubes = generate_cube_numbers(numbers)

    numbers_dataframe = pd.DataFrame({
        'Number': numbers,
        'Square': squares,
        'Cube': cubes
    } , index=range(START_COLUMN_NUMBER, END_COLUMN_NUMBER))

    print(numbers_dataframe)


if __name__ == "__main__":
    main()