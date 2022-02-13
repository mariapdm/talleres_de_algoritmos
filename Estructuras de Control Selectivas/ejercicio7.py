"""
Datos de entrada
numero_kilomentros->nk-->int
Datos de salida
cobro--co-->float
"""
#Entradas
nk=int(input("Ingrese la cantidad de kilometros: "))
#Caja negra
x=300
if(nk<=300):
    co=50000    
elif(nk>300 and nk<=1000):
    co=70000+(30000*(nk-300))
elif(nk>1000):
    co=150000+(9000*(nk-1000)+(30000*(nk-300)))
#Salida
print("El saldo a pagar es: ", co)