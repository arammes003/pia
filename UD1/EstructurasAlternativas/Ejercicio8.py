# Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, 
# proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa 
# será una de las siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), 
# «Notable» (nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), 
# «Matrícula de Honor» (nota 10).

# Funcion que pide la calificacion
def pedirCalificacion():
    try:
        nota = float(input("Introduce la calificacion: "))
        return nota
    except ValueError:
        return None
    
# Funcion que dependiendo de la nota califica numericamente
def calificarNota(nota):
    match nota:
        case _ if nota < 5:
            return "Suspenso"
        case _ if nota >= 5 and nota < 7:
            return "Aprobado"
        case _ if nota >= 7 and nota < 9:
            return "Notable"
        case _ if nota >= 9 and nota < 10:
            return "Sobresaliente"
        case _ if nota == 10:
            return "Matricula de honor"
        case _:
            return "No hay manera de calificar esto"
        
# Funcion principal
#   1. Obtenemos la nota a calificar
#   2. Obtenemos la calificacion
def main():
    nota = pedirCalificacion()
    if nota is None:
        print("Buenisma nota si señor...")
        return
    
    calificacion = calificarNota(nota)
    print(f"Tu nota {nota} es equivalente a {calificacion}")

# Llamada a la funcion principal
main()