"""
Datos de entrada
edad_uno-->e1-->int
edad_dos-->e2-->int
edad_tres-->e3-->int
Datos de salida
promedio-->p-->float
"""
#Entradas
e1=int(input("Ingrese la edad de la primera persona: "))
e2=int(input("Ingrese la edad de la segunda persona: "))
e3=int(input("Ingrese la edad de la tercera persona: "))
#Caja negra
p=(e1+e2+e3)/3
#Salidas
print("El promedio de edad de los tres es: ", p)