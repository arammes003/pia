# 6. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

# 5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista de 4 filas por 5 columnas. 
# El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. La suma total debe aparecer en la esquina inferior derecha.'

import numpy as np

def generate_matrix_random_nums():
    return np.random.randint(100, 999, (4, 5))

def create_sheet(matrix):
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    total_sum = np.sum(matrix)

    # Create a 5x6 matrix to include sums
    sheet = np.zeros((matrix.shape[0] + 1, matrix.shape[1] + 1), dtype=int)

    sheet[:-1, :-1] = matrix        # original matrix
    sheet[:-1, -1] = row_sums       # last column: row sums
    sheet[-1, :-1] = col_sums       # last row: column sums
    sheet[-1, -1] = total_sum       # bottom-right corner: total sum

    return sheet

def print_sheet(sheet):
    print("Sheet with sums:\n")
    for row in sheet:
        for value in row:
            print(f"{value:>5}", end=" ")
        print()

def main():
    matrix = generate_matrix_random_nums()
    print("Original matrix:\n")
    print(matrix)
    print()

    sheet = create_sheet(matrix)
    print_sheet(sheet)


main()