"""
Datos de entrada
monto_presupuesto—>mp—>int
Datos de salida
monto_ginecologia—>mg—>float
monto_traumatologia—>mt—>float
monto_pediatra—>md—>float
"""
#Entradas
mp=int(input("Ingrese el monto presupuestado: "))
#Caja negra
mg=mp*0.4
mt=mp*0.3
md=mp*0.3
#Salidas
print("El presupuesto para Ginecolgía es de: ", mg)
print("El presupuesto para Traumatología es de: ", mt)
print("El presupuesto para Pedriatría es de: ", md)