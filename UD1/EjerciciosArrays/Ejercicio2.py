"""
    Program: Do the previous exercise using numpy and taking advantage of its advantages
    Author: Alfonso Ramírez Mestanza
    Date: 05/11/2025
"""

import numpy as np
import pandas as pd

MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 100
NUMBERS_COUNT = 20
START_COLUMN_NUMBER = 1
END_COLUMN_NUMBER = 20 + 1

def generate_numbers(numbers_count):
    return np.random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER, numbers_count)

def main():
    numbers = generate_numbers(NUMBERS_COUNT)
    squares = numbers ** 2
    cubes = numbers ** 3

    numbers_dataframe = pd.DataFrame({
        'Number': numbers,
        'Square': squares,
        'Cube': cubes
    }, index = np.arange(START_COLUMN_NUMBER, END_COLUMN_NUMBER))

    print(numbers_dataframe)

if __name__ == "__main__":
    main()