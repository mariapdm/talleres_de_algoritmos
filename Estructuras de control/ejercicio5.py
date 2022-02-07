"""
Datos de entrada
parciales-->p-->float
examen_final-->ef-->float
trabajo_final-->tf-->float
Datos de salida
calificacion_final-->cf-->float
"""
#Entradas
p=int(input("Ingrese el promedio de los parciales: "))
ef=int(input("Ingrese la calificación del examen final: "))
tf=int(input("Ingrese la calificación del trabajo final"))
#Caja negra
capa=(p*0.55)
exfn=(ef*0.30)
trfn=(tf*0.15)
cf=(capa+exfn+trfn)
#Salidas
print("La calificación final de la materia es: ", cf)