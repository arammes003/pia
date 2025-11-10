from EjerciciosPOO.Ejercicio2.Fracciones import Fraction

# Prueba de la clase
def main():
    try:
        print("---------------SUMMARY---------------")
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        print(f"Summary f1 + f2 = {f1 + f2}")
        print(f"Inverted summary f2 + f1 = {f2 + f1}")

        print("-------------SUBTRACT----------------")
        print(f"Subtract f1 - f2 = {f1 - f2}")
        print(f"Inverted subtract f2 - f1 = {f2 - f1}")

        print("-----------MULTIPLICATION------------")
        print(f"Multiplation f1 * f2 = {f1 * f2}")
        print(f"Inverted multiplication f2 + f1 = {f2 * f1}")

        print("-------------DIVISION----------------")
        print(f"Division f1 / f2 = {f1 // f2}")
        print(f"Inverted division = {f2 // f1}")

        print("---------COMBINED OPERATIONS---------")
        print(f"{f1 + 1.5 * f2 // f1 - 4.5}")

        print("------------COMPARISIONS-------------")
        print(f"f1 == f2: {f1 == f2}")
        print(f"f1 != f2: {f1 != f2}")
        print(f"f1 < f2: {f1 < f2}")
        print(f"1 < f1: {1 < f1}")
        print(f"0.5 == f1: {0.5 == f1}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()