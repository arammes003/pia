# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

# Funcion que pide el dia de la semana
def pedirDia():
    try:
        dia = int(input("Introduce el dia de la semana (1-7): "))
        if dia >= 1 and dia <= 7:
            return dia

        return None
    except ValueError:
        return None
    
# Funcion que dice el dia 
def mostrarDia(dia):
    match dia:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")

# Funcion principal
#   1. Pedimos dia
#   2. Comprobamos que sea un dia valido
#   3. Mostramoos el dia de la semana que es
def main():
    dia = pedirDia()
    if dia is None:
        print("Po no sabia que habia mas de 7 dias a la semana. ERROR")

    
    mostrarDia(dia)

# Llamada a la funcion
main()