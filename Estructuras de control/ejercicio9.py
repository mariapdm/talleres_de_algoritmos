"""
Datos de entrada
horas_trabajadas-->ht-->int
precio_hora-->ph-->int
Datos de salida
salario_neto-->sn-->int
"""
#Entradas
ht=int(input("Ingrese el numero de horas trabajadas: "))
ph=int(input("Ingrese el precio por hora: "))
#Caja negra
t=ht*ph
p=t*0.2
sn=t-p
#Salidas
print("El salario neto del trabajador es de: ", sn)