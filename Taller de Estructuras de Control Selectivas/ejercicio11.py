"""
Datos de entrada
temperatura-->temp-->float
Datos de salidas
deporte-->dep-->string
"""
#Entradas
temp=float(input("Ingrese la temperatura en °F: "))
#Caja negra
deporte=""
if(temp>85 and temp<=120 ):
    deporte="natacion"
elif(temp>70 and temp<=85 ):
    deporte="tennis"
elif(temp>32 and temp<=70 ):
    deporte="golf"
elif(temp>10 and temp<=32 ):
    deporte="esqui"
elif(temp>0 and temp<=10 ):
    deporte="marcha"
else:
    deporte="no se encuentra en le rango"  
# salida
print("Su deporte es:", deporte)