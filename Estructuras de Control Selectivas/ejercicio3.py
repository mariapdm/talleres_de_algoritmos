"""
Datos de entrada
dato_uno-->a-->int
dato_dos-->b-->int
dato_tres-->c-->int
dato_cuatro-->d-->int
Datos de salida
algoritmo-->al-->float
"""
#Entrada
a=int(input("Ingrese el 1er número: "))
b=int(input("Ingrese el 2do número: "))
c=int(input("Ingrese el 3er número: "))
d=int(input("Ingrese el 4to número: "))
#Caja negra
if (d==0):
    al=(a-c)**2
elif (d>0):
    al=((a-b)**3)/d
#Salida
print("El valor es: ", al)
