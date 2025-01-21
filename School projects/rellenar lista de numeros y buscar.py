"""
Fecha: 3 de diciembre
Programador: Sergi
Descripcion: ejemplo de uso de listas bidireccionales
"""
import os
os.system("cls")
numeros=[]
for i in range(4):
    numeros.append(int(input("introduce un numero: ")))
encontrado=0
pos=[]
buscar=int(input("introduce el numero a buscar: "))
for i in range(4):
    if buscar==numeros[i]:
        pos.append(i+1)
    
        

if pos!=[]:
    print("tu numero esta en la posicion",pos)
else:
    print("el numero no esta en la lista")