"""
Datos de entrada
fecha_nacimiento-->fn-->float
Datos de salida
Edad-->dd-->int
signo_zodiacal-->sz-->string
"""
#Entradas
fn=input("Ingrese su fecha de nacimiento en formate dd/mm/yy: " )
day, month, year=fn.split("/")
dia_nacimiento=int(day)
mes_nacimiento=int(month)
año_nacimiento=int(year)
#Caja negra
import datetime
x=datetime.datetime.now()
mes_actual=int(x.strftime("%m"))
año_actual=int(x.strftime("%Y"))
dia_actual=int(x.strftime("%d"))
if(dia_actual>=dia_nacimiento and mes_actual>=mes_nacimiento):
    años=(año_actual-año_nacimiento)
else: 
    años=(año_actual-año_nacimiento-1)
signo=""
if ((mes_nacimiento==11) and (dia_nacimiento>=22)) or ((mes_nacimiento==12) and (dia_nacimiento<=21)):
    signo="Sagitario"
if ((mes_nacimiento==12) and (dia_nacimiento>=22)) or ((mes_nacimiento==1) and (dia_nacimiento<=20)):
    signo="Capricornio "
if ((mes_nacimiento==1) and (dia_nacimiento>=21)) or ((mes_nacimiento==2) and (dia_nacimiento<=19)):
    signo="Acuario "
if ((mes_nacimiento==2) and (dia_nacimiento>=20)) or ((mes_nacimiento==3) and (dia_nacimiento<=19)):
    signo="Piscis"
if ((mes_nacimiento==3) and (dia_nacimiento>=21)) or ((mes_nacimiento==4) and (dia_nacimiento<=20)):
    signo="Aries"
if ((mes_nacimiento==4) and (dia_nacimiento>=21)) or ((mes_nacimiento==5) and (dia_nacimiento<=21)):
    signo="Tauro"
if ((mes_nacimiento==5) and (dia_nacimiento>=22)) or ((mes_nacimiento==6) and (dia_nacimiento<=21)):
    signo="Geminis"
if ((mes_nacimiento==6) and (dia_nacimiento>=22)) or ((mes_nacimiento==7) and (dia_nacimiento<=22)):
    signo="Cancer"
if ((mes_nacimiento==7) and (dia_nacimiento>=23)) or ((mes_nacimiento==8) and (dia_nacimiento<=23)):
    signo="Leo"
if ((mes_nacimiento==8) and (dia_nacimiento>=24)) or ((mes_nacimiento==9) and (dia_nacimiento<=22)):
    signo="Virgo"
if ((mes_nacimiento==9) and (dia_nacimiento>=23)) or ((mes_nacimiento==10) and (dia_nacimiento<=22)):
    signo="Libra"
if ((mes_nacimiento==10) and (dia_nacimiento>=23)) or ((mes_nacimiento==11) and (dia_nacimiento<=21)):
    signo="Escorpion"
# Datos de Salida
print("Su signo zodiacal es: ", signo)
print(f"Tiene {años} años")