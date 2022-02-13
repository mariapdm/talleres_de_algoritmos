"""
Datos de entrada
lectura_actual-->lac-->int
lectura_anterior-->lec-->int
Datos de salida
monto_pagar-->mp-->float
"""
#Entrada
lac=int(input("Ingrese la lectura actual: "))
lec=int(input("Ingrese la lectura anterior: "))
#Caja negra
lnc=lec-lac
if(lnc>=0) and (lnc<=100):
    mp=lnc*4600
elif(lnc>=101) and (lnc<=300):
    mp=lnc*80000
elif(lnc>=301) and (lnc<=500):
    mp=lnc*100000
elif(lnc>=501):
    mp=lnc*120000
#Salida
print("El monto a pagar sera: ", mp)
