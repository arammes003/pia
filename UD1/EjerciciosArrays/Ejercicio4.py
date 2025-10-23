# 4. Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. 
# El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.

# Function that obtains the list of numbers from user input
def get_values(amount_of_numbers):
    numbers = []

    for _ in range(amount_of_numbers):
        numbers.append(int(input("Enter a number: ")))

    return numbers

# Function that rotate elements in the list
def rotate_elements(number_list):
    last_number = number_list[-1]

    rotated_list = [last_number] + number_list[:-1]
    return rotated_list

# Main function
def main():
    numbers = get_values(5)

    print(f"Original list: {numbers}")
    print(f"Rotated list: {rotate_elements(numbers)}")

# Call the main function
main()