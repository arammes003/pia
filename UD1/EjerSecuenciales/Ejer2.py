# 2. Calcular el perí­metro y área de un rectángulo dada su base y su altura.
def perimetro(l):
    return l + l + l;

def area(b, h):
    return (b * h) / 2

lado = int(input("Introduce la base del triangulo: "));
altura = int(input("Introduce la altura del triangulo: "));

print(f"El perímetro del triángulo con base {lado} es de {perimetro(lado)} cm")
print(f"El área del triangulo con base {lado} y altura {altura} es de {area(lado, altura)} cm2")
