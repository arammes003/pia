"""
    1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube.
    Carga las lista number con valores aleatorios entre 0 y 100.
    En la lista square se deben almacenar los cuadrados de los valores que hay en number.
    En la lista cube se deben almacenar los cubos de los valores que hay en number.
    A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

    Author: Alfonso Ramirez Mestanza
    Date: 21/11/2025
"""
import numpy as np

def get_number_list():
    return np.random.randint(0, 101, 20)

def get_square_numbers_list(numbers):
    return numbers ** 2

def get_cube_numbers_list(numbers):
    return numbers ** 3

def main():
    numbers = get_number_list()
    square_numbers = get_square_numbers_list(numbers)
    cube_numbers = get_cube_numbers_list(numbers)


if __name__ == "__main__":
    main()