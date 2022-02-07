"""
Datos de entrada
lado_uno-->a-->int
lado_dos-->b-->int
lado-->c-->int
Datos de salida
Area-->a-->float
"""
#Entradas
a=int(input("Ingrese la medida del lado a: "))
b=int(input("Ingrese la medida del lado b: "))
c=int(input("Ingrese la medida del lado c: "))
#Caja negra
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**(1/2)
#Salida
print("El area del triangulo es ", a)