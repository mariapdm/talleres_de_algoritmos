"""
Datos de entrada
ventas_totales-->vt-->float
departamento_uno-->du-->float
departamento_dos-->dd-->float
departamento_tres-->dt-->float
salario_mensual-->sm-->float
Datos de salida
sueldo_dep_uno-->sdu-->float
sueldo_dep_dos-->sdd-->float
sueldo_dep_tres-->sdt-->float
"""
#Entradas
vt=float(input("Ingrese las ventas totales: "))
du=float(input("Ingrese las ventas del departamento uno: "))
dd=float(input("Ingrese las ventas del departamento dos: "))
dt=float(input("Ingrese las ventas del departamento uno: "))
sm=float(input("Ingrese el salario bruto mensual: "))
#Caja negra
pp=vt*0.33
sb=sm*0.20
if(du>pp):
    sdu=sm+sb
else: 
    sdu=sm
if(dd>pp):
    sdd=sm+sb
else:
    sdd=sm
if(dt>pp):
    sdt=sm+sb
else: 
    sdt=sm
#Salidas
print("El departamento uno ganara: ", sdu)
print("El departamento dos ganara: ", sdd)
print("El departamento tres ganara: ", sdt)