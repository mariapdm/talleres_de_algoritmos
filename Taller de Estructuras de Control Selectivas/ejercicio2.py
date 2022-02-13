"""
Datos de entrada
sueldo_trabajador-->st-->float
Datos de salida
nuevo_sueldo-->ns-->float
"""
#Entrada
st=float(input("Ingrese el sueldo del trabajador: "))
#Caja negra
if (st<900000):
    s=st*0.15
    sm=st+s
else:
    s=st*0.12
    sm=st+s
#Salida
print("El nuevo salario sería: ", sm)