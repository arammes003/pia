"""
    Program: Create a program that show in screen N first prime numbers. N value is introduced by the user
    Author: Alfonso Ramírez Mestanza
    Date: 05/11/2025
"""

def get_quantity_numbers():
    return int(input("How much prime numbers do you want to get?: "))


def get_prime_numbers(numbers_quantity):
    prime_numbers = []

    cont = 2
    while len(prime_numbers) < numbers_quantity:
        is_prime = True

        for i in range(2, int(cont ** 0.5) + 1):
            if cont % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(cont)
        
        cont += 1
    
    return print(prime_numbers)
    

def main():
    quantity_numbers = get_quantity_numbers()
    get_prime_numbers(quantity_numbers)

if __name__ == "__main__":
    main()