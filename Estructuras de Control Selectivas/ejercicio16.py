"""
Datos de entrada
valor_uno-->a-->float
valor_dos-->b-->float
valor_tres-->c-->float
valor_cuatro-->x-->float
Datos de salida
valor_final-->vf-->float
"""
#Entrada
a=float(input("Digite el valor de A: "))
b=float(input("Digite el valor de B: "))
c=float(input("Digite el valor de C: "))
#Caja negra
from cmath import sqrt
d=(b**a-4*a*c)
if(d==0):
    x1=x2=-b(2*a)
elif(d>0):
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
else:
    x1=x2="No tiene solucion en los reales"
#Salidas
print("X1 es: ", x1)
print("X2 es: ", x2)