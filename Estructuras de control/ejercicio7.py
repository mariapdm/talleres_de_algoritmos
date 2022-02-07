"""
Datos de entrada
metros-->me-->float
Datos de salida
pulgadas-->das-->float
pies-->ft-->float
"""
#Entradas
me=float(input("Ingrese el valor en metros: "))
#Caja negra
das=(me*39.37)
ft=das/12
#Salidas
print("El valor en pulgadas equivale a: ", das)
print("El valor en pies equivale a: ", ft)