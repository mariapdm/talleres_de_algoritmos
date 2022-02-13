"""
Datos de salida
hemoglobina-->hm-->float
sexo-->sx-->string
edad-->ed-->int
Datos de entrada
anemia-->anm-->string
"""
#Entrada
hm=int(input("Ingrese el nivel de hemoglobina: "))
sx=int(input("Ingrese su sexo (1 para femenino y 2 para masculino): "))
ed=int(input("Ingrese su edad en meses: "))
#Caja negra
anemia=""
if(ed>=0 and ed<=1) and (hm>=13 and hm<=26):
    anemia="No tiene anemia"
elif(ed>1 and ed<=6) and (hm>=10 and hm<=18):
    anemia="No tiene anemia"
elif(ed>6 and ed<=12) and (hm>=11 and hm<=15):
    anemia="No tiene anemia"
elif(ed>12 and ed<=60 ) and (hm>=11.5 and hm<=15):
    anemia="No tiene anemia"
elif(ed>60 and ed<=120) and (hm>=12.6 and hm<=15.5):
    anemia="No tiene anemia"
elif(ed>120 and ed<=180) and (hm>=13 and hm<=15.5):
    anemia="No tiene anemia"
elif(ed>180) and (hm>=12 and hm<=16) and (sx==1):
    anemia="No tiene anemia"
elif(ed>180) and (hm>=14 and hm<=18) and (sx==2):
    anemia="No tiene anemia"
else:
    anemia="Tiene anemia"
#Salida
print("Su resultado es: ", anemia)
