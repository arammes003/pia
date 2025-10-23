# 5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista de 4 filas por 5 columnas. 
# El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. La suma total debe aparecer en la esquina inferior derecha.'

import random

def generate_matrix_random_nums():
    matrix = []

    for _ in range(4):
        row = []

        for _ in range(5):
            num = random.randint(100, 999)
            row.append(num)

        matrix.append(row)

    return matrix

def create_sheet(matrix):
    row_sums = []

    for row in matrix:
        sum = 0

        for num in row:
            sum += num
        
        row_sums.append(sum)

    col_sums = []
    num_columns = len(matrix[0])
    num_rows = len(matrix)

    for i in range(num_columns):
        sum = 0
        for j in range(num_rows):
            sum += matrix[j][i]
        col_sums.append(sum)
        
    total_sum = 0
    for sum in row_sums:
        total_sum += sum

    sheet = []
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            row.append(matrix[i][j])
        row.append(row_sums[i])
        sheet.append(row)

    last_row = []
    for sum in col_sums:
        last_row.append(sum)

    last_row.append(total_sum)
    sheet.append(last_row)

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
    for row in matrix:
        print(row)
    print()

    sheet = create_sheet(matrix)
    print_sheet(sheet)


main()