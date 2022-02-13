"""
Datos de entrada
cantidad_invertida-->ci-->float
interese-->int-->float
Datos de salida
dinero_final-->df--float
"""
#Entradas
ci=float(input("Ingrese la cantidad de dinero invertida: "))
int=float(input("Ingrese el porcentaje de interes: "))
#Caja negra
nt=ci*int/100
if (nt>100000):
    df=ci+nt
else:
    df=ci
#Salida
print("El dinero final en su cuenta es de: ", df)
