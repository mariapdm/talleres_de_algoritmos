archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la letra M
"""
m=0
lista=[]
ciudadm=[]
for i in archivo:
  e=i.index(":")
  for q in range(e+2, len(i)-1):
    lista.append(i[q])
    e="".join(lista)
  ciudadm.append(e)
  lista=[]
for i in ciudadm:
  if(i[0]=="M"):
    m=m+1
print(m)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U  
"""
lista=[]
lista2=[]
ciudadu=[]
paisu=[]
for i in archivo:
  e=i.index(":")
  for q in range(e+2, len(i)-1):
    lista.append(i[q])
    e="".join(lista)
  ciudadu.append(e)
  lista=[]
  n=i.index(":")
  for t in range(0, n):
    lista2.append(i[t])
    n="".join(lista2)
  paisu.append(n)
  lista2=[]
for i in paisu:
  if(i[0]=="U"):
    print(i) 
for i in ciudadu:
  if(i[0]=="U"):
    print(i)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
a=0
lista=[]
for i in archivo:
  lista.append(i)   
  a=a+1
print(a)
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
sin=[]
for i in archivo: 
  p=i.index(":")
  for g in range(p+2, len(i)-1):
    lista.append(i[g])
    p="".join(lista)
  sin.append(p)
  lista=[]
for i in sin:
  if(i=="Singapur"):
    print(i)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo: 
    lista.append(i)
    if(i=="Venezuela: Caracas\n"):
      print(i)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
d=0
lista=[]
ciudade=[]
ciudadp=[]
for i in archivo:
  lista.append(i)
for i in lista:  
  if(i[0]=="E"):
    ciudade.append(i)
    d=d+1
  print(d)
  c="".join(ciudade)  
for i in ciudade:
  a=i.index(":")     
  for q in range(a+2,len(i)-1):
    ciudadp.append(i[q])
  b="".join(ciudadp)  
  for t in ciudadp:
    t="".join(ciudadp)
  ciudadp=[]
  print(t)
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
cap=[]
for i in archivo: 
  b=i.index(":")
  for o in range(b+2, len(i)-1):
    lista.append(i[o])
    b="".join(lista)
  cap.append(b)
  lista=[]
for i in cap:
  if(i=="Bogotá"):
    print(i)
"""
#imprima la posicion del pais de Uganda
"""
u=0
lista=[]
for i in archivo:
  lista.append(i)
  g=" ".join(lista)
  u=u+1 
  if(g=="Uganda: Kampala\n"):
    break
  lista=[]   
print(u)
"""
#imprima la posicion del pais de Mexico
"""
m=0
lista=[]
for i in archivo:
  lista.append(i)
  x=" ".join(lista)
  m=m+1
  if(x=="México: Ciudad de México \n"):
    break
  lista=[]
print(m)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
for i in archivo:
  lista.append(i)
lista.remove("Madagascar: rey julien\n")
lista.insert(109,"Madagascar: Antananarivo\n")
print(lista)
""" 
#Agregue un país que no esté en la lista
"""
lista=[]
for i in archivo:
  lista.append(i)
lista.insert(97,"Kosovo: Pristina\n")
print(lista)
"""
archivo.close()
