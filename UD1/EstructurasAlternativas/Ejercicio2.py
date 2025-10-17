# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#   1. Si se cumple Pitágoras entonces es triángulo rectángulo
#   2. Si sólo dos lados del triángulo son iguales entonces es isósceles.
#   3. Si los 3 lados son iguales entonces es equilátero.
#   4. Si no se cumple ninguna de las condiciones anteriores, es escaleno.

# Funcion que pide las entradas del triangulo
def pedirDatos():
    entradaA = float(input("Introduce la medida del lado 1: ")) 
    entradaB= float(input("Introduce la medida del lado 2: ")) 
    entradaC = float(input("Introduce la medida del lado 3: ")) 

    return entradaA, entradaB, entradaC


# Funcion que comprueba que es rectangulo cumpliendo el teorema de pitagoras
def esRectangulo(lado1, lado2, lado3):
    lados = [lado1, lado2, lado3]
    hipotenusa = max(lados)

    return hipotenusa**2 == lado1**2 + lado2**2


# Funcion que comprueba que es isosceles
# - 2 lados iguales y 1 distinto
def esIsosceles(lado1, lado2, lado3):
    if lado1 == lado2 != lado3:
        return lado1 == lado2 != lado3
    elif lado1 == lado3 != lado2:
        return lado1 == lado3 != lado2
    elif lado2 == lado3 != lado1:
        return lado3 == lado2 != lado1
    return


# Funcion que comprueba que sea equilatero
# - Todos los lados iguales
def esEquilatero(lado1, lado2, lado3):
    return lado1 == lado2 == lado3


# Funcion principal
#   1. Pedimos los datos
#   2. Comprobamos el tipo de triangulos
def main():
    a, b, c = pedirDatos()

    if esEquilatero(a, b, c):
        print("El triangulo es equilatero.")
    elif esRectangulo(a,b,c):
        print("El triangulo es rectangulo")
    elif esIsosceles(a, b, c):
        print("El triangulo es isosceles")
    else:
        print( "El triangulo es escaleno")

# Llamada al programa
main()