# Crea un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización después de que se pida al usuario/a:

#   1. Importe del préstamo.
#   2. La tasa de interés anual.
#   3. Y el plazo de pago en años.

# Funcion que pide el importe del prestamo
def importePrestamo():
    try:
        prestamo = float(input("Introduce el importe del prestamo: "))
        return prestamo
    except ValueError:
        print("No sabia que prestaban cosas que no son numeros...")
        return None
    
# Funcion que pide la tasa de interes anual
def tasaInteresAnual():
    try:
        tasa = float(input("Introduce la tasa de interes anual: "))
        return tasa
    except ValueError:
        print("No sabia que las tasas no son numeros...")
        return None

# Funcion que pide el plazo de pago en años
def pedirNumeroPlazos():
    try:
        plazos = int(input("Introduce la cantidad de plazos: "))
        return plazos
    except ValueError:
        print("No sabia que los plazos no son numeros...")
        return None
    
# Funcion que calcula la cuota de la hipoteca\
#   1. r = Interes anual
#   2. n = plazos
def calcularHipoteca(prestamo, tasaInteres, plazosAnuales):
    r = tasaInteres / 100 
    n = plazosAnuales
    cuota = prestamo * r * (1 + r)**n / ((1 + r)**n - 1)
    return cuota

# Funcion que calcula la tabla de amortizacion
# - Obtenemos la cuota
# - Creamos una tabla
# - Bucle que muestra año a año la cuota, los intereses, la amortizacion y el prestamo que le queda pendiente 
def tablaAmortizacion(prestamo, tasaInteres, plazosAnuales):
    interesAnual = tasaInteres / 100
    cuota = calcularHipoteca(prestamo, tasaInteres, plazosAnuales)

    print(f"{'Año':<5}{'Cuota':<12}{'Interés':<12}{'Amortización':<15}{'Pendiente':<12}")
    print("-" * 60)

    for año in range(1, plazosAnuales + 1):
        interes = prestamo * interesAnual
        amortizacion = cuota - interes
        prestamo -= amortizacion
        print(f"{año:<5}{cuota:<12.2f}{interes:<12.2f}{amortizacion:<15.2f}{prestamo:<12.2f}")

# Funcionm principal
#   1. Pedimos el prestamo
#   2. Pedimos la tasa de intereses
#   3. Pedimos la cantiddd de plazos
#   4. Obtenemos la cuota de la hipoteca
#   5. Imprimimos la tabla de amortizacion 
def main():
    prestamo = importePrestamo()
    tasa = tasaInteresAnual()
    plazos = pedirNumeroPlazos()

    hipoteca = calcularHipoteca(prestamo, tasa, plazos)
    print(f"La cuota de la hipoteca es de: {hipoteca:.2f}")

    tablaAmortizacion(prestamo, tasa, plazos)

# Llamada al ejercicio
main()