"""
Datos de entrada
lectura_anterior-->la-->float
lectura actual-->lt-->float
valor_kilovatio-->kw-->float
Datos de salida
valor_pagar-->vp-->float
"""
#Entradas
la=float(input("Digita la lectura anterior del medidor: "))
lt=float(input("Digite la lectura actual del medidor: "))
kw=float(input("Digite el valor por kilovatio: "))
#Caja negra
kv=(la+lt)*kw
#Salidas
print("El monto total a pagar del mes es de: ", kw)