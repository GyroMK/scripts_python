# Fecha: 3 de diciembre
# Programador: Sergi
# Descripcion: ejemplo de uso de listas bidireccionales

import os

os.system("cls")

num=[]
for i in range(5):
    num.append(int(input("escribe un numero: ")))
    if num[i] % 2 !=0:
        print(num[i],"es impar")
    else:
        print(num[i],"es par")
