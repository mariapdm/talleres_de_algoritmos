"""
Datos de entrada
Cantidad_prestamo—>cr—>float
Datos de salida
porcentaje_anual—>pa—>float
Intereses—>inr—>float
"""
#Entrada
cr=int(input("Ingrese la cantidad del prestamo: "))
#Caja negra
pa=(cr*4)/100
#Salida
print("El porcentual anual es de: ", pa)