"""
Datos de entrada
numero_de_billetes_50000--->n1-->int
numero_de_billetes_20000--->n2-->int
numero_de_billetes_10000--->n3-->int
numero_de_billetes_5000--->n4-->int
numero_de_billetes_2000--->n5-->int
numero_de_billetes_1000--->n6-->int
numero_de_billetes_500--->n7-->int
numero_de_billetes_100--->n8-->int
Datos de salida
Dinero_total-->dnt-->float
"""
#Entradas
n1=int(input("Número de billetes de 50000: "))
n2=int(input("Número de billetes de 20000: "))
n3=int(input("Número de billetes de 10000: "))
n4=int(input("Número de billetes de 5000: "))
n5=int(input("Número de billetes de 2000: "))
n6=int(input("Número de billetes de 1000: "))
n7=int(input("Número de billetes de 500: "))
n8=int(input("Número de billetes de 100: "))
#Caja negra
dnt=(n1*50000)+(n2*20000)+(n3*10000)+(n4*5000)+(n5*2000)+(n6*1000)+(n7*500)+(n8*100)
#Salidas
print("El dinero total que contiene el banco es de: ", dnt)