"""
    En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan,
    vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

    - Crear duraciones de tiempos.
        * Ejemplo: t = Duration(10,20,56)
        * Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
        * Si no indico la hora, minuto o segundo estos valores son cero:
            Duration() --> (0, 0, 0)
            Duration(34) --> (34, 0, 0)
            Duration(34, 15) --> (34, 15, 0)
            Duration(34, 61) --> (35, 1, 0)
    - Las duraciones de tiempo se pueden comparar.
    - A las duraciones de tiempo les puedo sumar y restar segundos.
    - Las duraciones de tiempo se pueden sumar y restar.

    Author: Alfonso Ramírez Mestanza
    Date: 27/10/2025
"""

class Duration:

    # Constructor
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__normalize_to_seconds()


    def __normalize_to_seconds(self):
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("Total seconds cannot be negative")

        self.__hours = seconds // 3600
        remaining = seconds % 3600
        self.__minutes = remaining // 60
        self.__seconds = remaining % 60


    # Devuelve la duración total en segundos (para comparar fácilmente)
    def __total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    # Getters
    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    # ToString
    def __str__(self):
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"


    # Comparaciones
    def __eq__(self, other):
        return self.__total_seconds() == other.__total_seconds()

    def __lt__(self, other):
        return self.__total_seconds() < other.__total_seconds()

    def __le__(self, other):
        return self.__total_seconds() <= other.__total_seconds()

    def __gt__(self, other):
        return self.__total_seconds() > other.__total_seconds()

    def __ge__(self, other):
        return self.__total_seconds() >= other.__total_seconds()

    def __ne__(self, other):
        return self.__total_seconds() != other.__total_seconds()

    # Sumar segundos
    def __add__(self, other):
        if isinstance(other, Duration):
            total = self.__total_seconds() + other.__total_seconds()
        elif isinstance(other, (int, float)):
            total = self.__total_seconds() + other

        return Duration(0,0,int(total))

    def __radd__(self, other):
        if isinstance(other, Duration):
            total = other.__total_seconds() + self.__total_seconds()
        elif isinstance(other, (int, float)):
            total = other + self.__total_seconds()

        return Duration(0, 0, int(total))

    def __sub__(self, other):
        if isinstance(other, Duration):
            total = self.__total_seconds() - other.__total_seconds()
        elif isinstance(other, (int, float)):
            total = self.__total_seconds() - other

        return Duration(0, 0, int(total))


# Main function
def main():
    try:
        d1 = Duration(10, 62, 15)
        print(f"La hora d1 es: {d1}")
    except ValueError as e:
        print(f"Error al crear d1: {e}")

    try:
        d2 = Duration(-10, -23, -24)
        print(f"La hora d2 es: {d2}")
    except ValueError as e:
        print(f"Error al crear d2: {e}")

    try:
        d3 = Duration(34, 15)
        print(f"La hora d3 es: {d3}")
    except ValueError as e:
        print(f"Error al crear d3: {e}")


    try:
        d4 = Duration(34, 15)
        print(f"La hora d4 es: {d4}")
        d5 = Duration(34, 15, 56)
        print(f"La hora d4 es: {d5}")

        # Comparaciones descriptivas:
        if d5 > d4:
            print(f"{d5} es mayor que {d4}")
        elif d5 < d4:
            print(f"{d5} es menor que {d4}")
        elif d5 == d4:
            print(f"{d5} es igual a {d4}")
    except ValueError as e:
        print(f"Error al crear d5: {e}")

    try:
        d6 = Duration(23, 67, 21)
        print(d6)
        d7 = 3674 + d6
        print(d7)
    except ValueError as e:
        print(e)

# Main
if __name__ == "__main__":
    main()