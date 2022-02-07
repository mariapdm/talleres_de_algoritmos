"""
Datos de entrada
nota_examen_ matematicas-->nem-->float
nota_ta1_matematicas-->ntm-->
nota_ta2_matematicas-->nttm-->
nota_ta3_matematicas-->ntttm-->
nota_examen_fisica-->nef-->float
nota_ta1_fisica-->ntf-->float
nota_ta2_fisica-->nttf-->float
nota_examen_quimica-->neq-->float
nota_ta1_quimica-->ntq-->float
nota_ta2_quimica-->nttq-->float
nota_ta3_quimica-->ntttq-->float
Datos de salida
Promedio_tres-->pt-->float
promedio_matematicas-->pm-->float
promedio_fisica-->pf-->float
promedio_quimica-->pq-->float
"""
#Entradas
nem=float(input("Ingrese la nota del examen de matemáticas: "))
ntm=float(input("Ingrese la nota de la 1ra tarea de matemáticas: "))
nttm=float(input("Ingrese la nota de la 2da tarea de matemáticas: "))
ntttm=float(input("Ingrese la nota de la 3ra tarea de matemáticas: "))
nef=float(input("Ingrese la nota del examen de física: "))
ntf=float(input("Ingrese la nota de la 1ra tarea de física: "))
nttf=float(input("Ingrese la nota de la 2da tarea de física: "))
neq=float(input("Ingrese la nota del examen de química: "))
ntq=float(input("Ingrese la nota de la 1ra tarea de química: "))
nttq=float(input("Ingrese la nota de la 2da tarea de química: "))
ntttq=float(input("Ingrese la nota de la 3ra tarea de química: "))
#Caja negra
pm=(nem*0.90)+(((ntm+nttm+ntttm)/3)*0.1)
pf=(nef*0.8)+(((ntf+nttf)/2)*0.2)
pq=(neq*0.85)+(((ntq+nttq+ntttq)/3)*0.15)
pt=(pm+pf+pq)/3
#Salidas
print("El promedio de las tres materias es: ", pt)
print("El promedio de matemáticas es: ", pm)
print("El promedio de física es: ", pf)
print("El promedio de química es: ", pq)