"""
Datos de entrada
monto_compra-->mc-->float
salida
cantidad_inv_fondos-->cif-->float
credito_a_pagar-->cp-->float
pago_interese-->pi-->float
cantidad_prestada-->cap-->float
"""
#Entradas
mc=float(input("Ingrese el valor de las piezas: "))
#Caja negra
if (mc>5000000):
    pd=(mc*0.55)
    pb=(mc*0.30)
    cf=(mc*0.15)
    pi=(cf*0.20)
elif (mc<5000000):
    pd=(mc*0.70)
    cf=(mc*0.30)
    pi=(cf*0.20)
    pb=0
#Salidas
print("La cantidad que se invierte de los fondos de la empresa es: ", pd)
print("La cantidad a pagar a credito es: ", cf)
print("El monto a pagar por intereses es: ", pi)
print("La cantidad que ha prestado el banco es: ", pb)
