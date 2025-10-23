# 2. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

import numpy as np
import pandas as pd

def define_list_number(cantity_numbers):
    numbers = np.random.randint(0, 100, cantity_numbers)

    return numbers

def main():
    numbers = define_list_number(20)
    squares = numbers ** 2
    cubes = numbers ** 3

    df = pd.DataFrame({
        'Number': numbers,
        'Square': squares,
        'Cube': cubes
    } , index=np.arange(1, 21))

    print(df)

main()