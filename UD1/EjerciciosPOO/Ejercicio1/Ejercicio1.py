from EjerciciosPOO.Ejercicio1.Duration import Duration

def main():
    try:
        d1 = Duration(27, 28, 203)
        d2 = Duration(3, 2, 92)
        d3 = d1 + d2
        print(d3)

        d4 = Duration(22, 3, 10)
        d5 = Duration(2, 3, 10)
        d6 = d4 - d5
        print(d6)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()