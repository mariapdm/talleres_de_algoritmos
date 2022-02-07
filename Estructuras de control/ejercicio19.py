"""
Datos de entrada
numero_naranjas--x-->int
valor_docena-->y-->float
dinero_obtenido-->k-->float
Datos de salida
porcentaje_ganancia-->pg-->float
"""
#Entradas
x=int(input("Ingrese la cantidad de naranjas: "))
y=float(input("Ingrese el valor de la docena: "))
k=float(input("Ingrese el dinero obtenido de la venta: "))
#Caja negra
n=(x/12)*6
p=(k-n)
pg=(p*100)/n
#Salida
print(f"El porcentaje de ganancia obtenida es de {pg}%")