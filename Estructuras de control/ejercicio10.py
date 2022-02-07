"""
Datos de entrada
chelines_austriacos-->ca-->float
dracmas griedos-->dg-->float
pesetas-->pes-->float
Datos de salida
pesetas-->tas-->float
francos_franceses-->ff-->float
dolar-->usd-->float
liras_italianas-->li-->float
"""
#Entradas
ca=float(input("Ingrese la cantidad de chelines austriacos: "))
dg=float(input("Ingrese la cantidad de dracmas griedos: "))
pes=float(input("Ingrese la cantidad de pesetas: "))
#Caja negra
tas=(ca*956.871)/100
f=(dg*88.607)/100
ff=f/20.110
usd=pes/122.499
li=(pes*100)/9.289
#Salidas
print("La cantidad de pesetas es: ", tas)
print("La cantidad de francos franceses: ", ff)
print("La cantidad de dolares es de: ", usd)
print("La cantidad de liras italianas es: ", li)
