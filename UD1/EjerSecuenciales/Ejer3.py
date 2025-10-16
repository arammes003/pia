# 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

def calcularHorasMinutos(minutosTotales):
    horas = minutosTotales // 60
    minutos = minutosTotales % 60
    return horas, minutos

minutos = int(input("Introduce una cantidad de minutos a convertir en horas y minutos: "))
horas, minutosRestantes = calcularHorasMinutos(minutos)


print(f"{minutos} equivalen a {horas} horas con {minutosRestantes} minutos")

