# funciones para manejo de listas
# vamos a crear las siguietes funciones
#   -rellenar lista: pedira el numero de elemtes y creara la lista
#   -mostrar lista: mostrara los elementos de la lista
#   -suma: sumara los elementos de la lista
#   -mayor: mostrara el elemento mayor de la lista
#   -menor: mostrara el elemento menor de la lista
#-------------------------------------------------------------------------

def rellenar(lista):
    cantidad=int(input("dime numero de elemtos de la lista: "))
    for num in range(cantidad):
        lista.append(int(input("dime el numero " + str(num+1) + ": ")))

def mostrar(lista):
    print(lista)

def suma(lista):
    suma = 0
    for num in range(len(lista)):
        suma += lista[num]
    print(suma)

def mayor(lista):
    mayor = lista[0]
    for num in range(len(lista)):
        if lista[num] > mayor:
            mayor = lista[num]
    print("el mayor es: ", mayor)

def menor(lista):
    menor = lista[0]
    for num in range(len(lista)):
        if lista[num] < menor:
            lista[0] = lista[num]
    print("el menor es: ", menor)

#---------------------------------------

import os
os.system("cls")

lista=[]
rellenar(lista)
mostrar(lista)
suma(lista)
mayor(lista)
menor(lista)