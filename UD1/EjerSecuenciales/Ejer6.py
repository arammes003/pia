# 6. Escribir un programa para calcular la nota final de un examen, considerando que:

# - Cada respuesta correcta suma 5 puntos.
# - Cada respuesta incorrecta suma -1 puntos.
# - Cada respuesta en blanco suma 0 puntos. 
# - Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

preguntasExamen = int(input("Cuantas preguntas tiene el examen: "))
respCorrectas = int(input("Cuantas preguntas son correctas: "))
respIncorrectas = int(input("Preguntas incorrectas: "))
respBlanco = int(input("Preguntas en blanco: "))

def obtenerPuntuacion(correctas, incorrectas, blanco, numPreguntas):
    puntuacion = (correctas * 5) + (incorrectas * -1)

    puntuacionMax = numPreguntas * 5;

    nota = (puntuacion / puntuacionMax) * 10;
    notaFinal = max(0, nota)

    print(f"Puntuacion: {puntuacion} puntos")
    print(f"Nota final: {notaFinal}/10")

obtenerPuntuacion(respCorrectas, respIncorrectas, respBlanco, preguntasExamen)