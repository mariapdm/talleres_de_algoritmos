"""
Datos de entrada
sueldo_base-->sb-->int
ventas-->v-->int
Datos de salida
comision-->c-->float
ganancia-->g-->float
"""
#Entradas
sb=int(input("Ingrese el sueldo base: "))
v=int(input("Ingrese el total de ventas: "))
#Caja negra
c=(v*0.10)
g=(sb*c)
#Salidas
print("Obtendra de comisiones: ", c)
print("Su sueldo total será de: ", g)