# Fecha: 3 de diciembre 2024
# Programador: Sergi
# Descripcion: Programa que lea 5 numeros y los guarde en una lista y los sume

import os
os.system("cls")
numeros = []
for i in range(5):
    numeros.append(int(input("escribe un numero: ")))
print(numeros)

suma=0
for i in range(5):
    suma=suma+numeros[i]
print(suma)