"""
Datos de entrada
nombre-->nom-->string
monto_comra-->mc-->float
Datos de salida
nombre-->nom-->string
monto_compra-->mp-->float
monto_pagar-->mg-->float
descuento-->de-->float
"""
#Entrada
nom=str(input("Ingrese nombre del cliente: "))
mc=float(input("Ingrese el monto de compra: "))
#Caja negra
if(mc<50000):
    mg=mc
    de=0
elif(mc>50000) and (mc<=100000):
    mgg=mc*0.05
    mg=mc-mgg
    de=0.05*100
elif(mc>100000) and (mc<=700000):
    mgg=mc*0.11
    mg=mc-mgg
    de=0.11*100
elif(mc>700000) and (mc<=1500000):
    mgg=mc*0.18
    mg=mc-mgg
    de=0.18*100
elif(mc>1500000):
    mgg=mc*0.25
    mg=mc-mgg
    de=0.35*100
#Salida
print("Nombre del cliente: ", nom)
print("El monto de compra es: ", mc)
print("El monto a pagar es: ", mg)
print(f"El descuento fue de: {de}%")