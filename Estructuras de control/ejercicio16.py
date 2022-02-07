"""
Datos de entrada
cantidad_galones—>cg—>float
Datos de salida
Cobro_cliente—>cc—>float
"""
#Entradas
cg=float(input("Ingrese la cantidad de galones:"))
#Caja negra
cv=(cg*3.785)
cc=(cv*50000)
#Salidas
print("El cliente debe pagar: ", cc)