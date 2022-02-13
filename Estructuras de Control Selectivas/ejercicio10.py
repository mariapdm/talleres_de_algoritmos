"""
Datos de entrada
categoria-->ctg-->int
sueldo_bruto-->sb-->float
Datos de salida
categorio-->ctg-->int
nuevo_saldo-->ns-->float
"""
#Entrada
ctg=int(input("Ingrese la categoria del trabajador: "))
sb=float(input("Ingrese el salario del trabajador: "))
#Caja negra
if(sb==900000):
    ns=(sb*0,60)+sb
    ctg=5
elif(sb==2000000):
    ns=(sb*0.40)+sb
    ctg=4
elif(sb==3600000):
    ns=(sb*0.20)+sb
    ctg=3
elif(sb==4300000):
    ns=(sb*0.15)+sb
    ctg=2
elif(sb==5000000):
    ns=(sb*0.10)+sb
    ctg=1
#Salidas
print("Categoria del trabajador: ", ctg)
print("El nuevo sueldo es: ", ns)