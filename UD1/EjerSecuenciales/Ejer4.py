# 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

numero = int(input("Introduce un numero de dos cifras: "))

def invertirNumero(numero):
    numeroStr = str(numero);
    return numeroStr[::-1]

print(f"El numero {numero} invertido es {invertirNumero(numero)}")