# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

HoraSalida = int((input("Introduzca la Hora de salida :")))
MinutoSalida = int((input("Introduzca el Minuto de salida :")))
SegundoSalida = int((input("Introduzca el Segundo de salida :")))

TiempoViaje = int(input("Introduzca el tiempo de viaje en segundos: "))

# Pasar unidades a segundos

TiempoSalida = ((HoraSalida * 3600)+(MinutoSalida*60)+SegundoSalida)

segFinal = (TiempoSalida + TiempoViaje)

print(f"La hora de llegada es {(segFinal // 3600)}")
print(f"La hora de llegada es {((segFinal % 3600) // 60)}")
print(f"La hora de llegada es {(segFinal % 3600) % 60}")

# Este programa es horrible, no se te ocurra volver a hacer algo así
