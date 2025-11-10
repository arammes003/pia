"""
    Crea una clase, y pruébala, que modele fracciones. Debe permitir:

    Crear fracciones indicando numerador y denominador.
     Ejemplo: f = Fraction(2, 3)
    Ojo!!! No se puede tener un denominador cero.
    Las fracciones pueden operar entre sí.
    Sumar, multiplicar, dividir, restar.
    Ojo!!! esto se puede hacer: f + 1, 5 * f
    Las fracciones se pueden comparar.
    ==, <, <=, >, >=, !=
    Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
    Ojo!!! esto se puede hacer 1 < 1/2

    Author: Alfonso Ramírez Mestanza
    Date: 29/10/2025
"""
from math import gcd
from fractions import Fraction as PyFraction  # para convertir floats a fracción


class Fraction():
    # Constructor
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("The denominator cannot be 0.")
        self.__numerator = numerator
        self.__denominator = denominator
        self.__simplify()

    def __simplify(self):
        common_denominator = gcd(self.__numerator, self.__denominator)
        self.__numerator //= common_denominator
        self.__denominator //= common_denominator
        # Mantener el signo en el numerador
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

    # String
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
            denominator = self.__denominator * other.__denominator
        elif isinstance(other, int):
            numerator = self.__numerator + other * self.__denominator
            denominator = self.__denominator
        elif isinstance(other, float):
            frac = PyFraction(other).limit_denominator(1000000)  # límite de denominador para precisión
            numerator = self.__numerator * frac.denominator + frac.numerator * self.__denominator
            denominator = self.__denominator * frac.denominator

        return Fraction(numerator, denominator)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            denominator = self.__denominator * other.__denominator
        elif isinstance(other, int):
            numerator = self.__numerator - other * self.__denominator
            denominator = self.__denominator
        elif isinstance(other, float):
            frac = PyFraction(other).limit_denominator(1000000)  # límite de denominador para precisión
            numerator = self.__numerator * frac.denominator - frac.numerator * self.__denominator
            denominator = self.__denominator

        return Fraction(numerator, denominator)

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
        elif isinstance(other, int):
            numerator = self.__numerator * other
            denominator = self.__denominator
        elif isinstance(other, float):
            frac = PyFraction(other).limit_denominator(1000000)
            numerator = self.__numerator * frac.numerator
            denominator = self.__denominator * frac.denominator

        return Fraction(numerator, denominator)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.__denominator
            denominator = self.__denominator * other.__numerator
        elif isinstance(other, int):
            numerator = self.__numerator
            denominator = self.__denominator * other
        elif isinstance(other, float):
            frac = PyFraction(other).limit_denominator(1000000)
            numerator = self.__numerator * frac.denominator
            denominator = self.__denominator * frac.numerator

        return Fraction(numerator, denominator)

    def __rfloordiv__(self, other):
        return self // other

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator == self.__denominator * other.__numerator
        elif isinstance(other, int):
            return self.__numerator == other * self.__denominator
        elif isinstance(other, float):
            return float(self.__numerator) / self.__denominator == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator < self.__denominator * other.__numerator
        elif isinstance(other, int):
            return self.__numerator < other * self.__denominator
        elif isinstance(other, float):
            return self.__numerator / self.__denominator < other
        else:
            return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other