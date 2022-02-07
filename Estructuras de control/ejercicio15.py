"""
Datos de entrada
precio_final-->pf-->int
precio_publico-->pp-->int
Datos de salida
descuento-->d-->float
"""
#Entradas
pf=int(input("Ingrese el precio final: "))
pp=int(input("Ingrese el precio al público: "))
#Caja negra
r=((pp-pf)/pp)*100
#Salidas
print(f"El porcentaje de descuento fue de: {r}%")