"""
Datos de entrada
precio_publico-->pp-->int
Datos de salida
precio_final-->pf-->int
"""
#Entradas
pp=int(input("Ingrese el precio al público: "))
#Caja negra
pf=pp-(pp*0.15)
#Salida
print("El valor final a pagar es de: ", pf)