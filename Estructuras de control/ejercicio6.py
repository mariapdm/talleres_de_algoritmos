"""
Datos de entrada
mujeres-->m-->int
hombres-->h-->int
Datos de salida
porcentaje_mujeres-->pm-->float
porcentaje_hombres-->ph-->float
"""
#Entradas
m=int(input("Ingrese el número de estudiantes mujeres: "))
h=int(input("Ingrese el número de estudiantes hombres: "))
#Caja negra
s=(m+h)
pm=(m*100)/s
ph=(h*100)/s
#Salida
print(f"El promedio de mujeres es de {pm}%")
print(f"El promedio de hombres es de {ph}%")