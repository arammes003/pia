# 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un programa que determine la hora de llegada a la ciudad B.

horaSalida = input("Introduce la hora de salida en HH:MM:SS: ")
tiempoViaje = int(input("Introduce la duracion del viaje en segundos: "))

def obtenerHoraLlegada(hora, duracionViaje):
    hh, mm, ss = map(int, hora.split(":"))

    if (hh < 0 or hh > 23 or mm < 0 or mm > 59 or ss < 0 or ss > 59):
        print(f"ERROR BROTHER, COMO QUE {hora} HORAS!!!!")
        return
    
    # Duracion viaje + hora salida
    totalSegundos = hh * 3600 + mm * 60 + ss + duracionViaje

    # Calcular nueva hora
    horaLlegada = totalSegundos % (24 * 3600) # Pa que no pase 24h
    hhLlegada = horaLlegada // 3600
    mmLlegada = (horaLlegada % 3600) // 60
    ssLlegada = horaLlegada % 60

    print(f"Hora estimada de llegada: {hhLlegada:02d}:{mmLlegada:02d}:{ssLlegada:02d}")  

obtenerHoraLlegada(horaSalida, tiempoViaje)