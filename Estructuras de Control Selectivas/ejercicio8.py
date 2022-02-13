"""
Datos de entrada
valor_uno-->p-->int
valor_dos-->q-->int
Datos de salida
satisfacen-->sa-->string
"""
#Entrada
p=int(input("Ingrese el primer valor: "))
q=int(input("Ingrese el segundo valor: "))
#Caja negra
respuesta=""
ec=(p**3+q**4-2*(p**2))
if(ec>680):
    print("P y Q satisfacen la expresión")
else:
    print("P y Q no satisfacen")