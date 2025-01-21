# Fecha: 26 de noviembre de 2024
# Programador: Sergi
# Descripcion: Este programa creara una lista oon 10 nombres

import os

os.system("cls")

"""var=5
nombres=[None]*var
for i in range(var):
    nombres[i]= str(input("escribe un nombre: "))


for e in range(var):
    nombres[e]=nombres[e].upper()
print(nombres)"""

var=5
numero=[None]*var
for i in range(var):
    numero[i]= str(input("escribe un numero: "))
may=numero[0]
for i in range(var):
    if may<numero[i]:
       may=numero[i]
print(may)