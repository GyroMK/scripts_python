import os

os.system("cls")
try:
    def rellenar(lista):
        try:
            cantidad=int(input("dime numero de elemtos de la lista: "))
            if cantidad < 0:
                print("El numero no puede ser menor que 0")
            for num in range(cantidad):
                lista.append(int(input("dime el numero " + str(num+1) + ": ")))
        except ValueError:
            print("escribe un numero valido")

    def mostrar(lista):
        print(lista)

    def suma(lista):
        suma = 0
        for num in range(len(lista)):
            suma += lista[num]
        print(suma)

    def mayor(lista):
        try:
            mayor = lista[0]
            for num in range(len(lista)):
                if lista[num] > mayor:
                    mayor = lista[num]
            print("el mayor es: ", mayor)
        except IndexError:
            print("se ha producido un error al mostrar el mayor")

    def menor(lista):
        try:
            menor = lista[0]
            for num in range(len(lista)):
                if lista[num] < menor:
                    lista[0] = lista[num]
            print("el menor es: ", menor)
        except IndexError:
            print("se ha producido un error al mostrar el menor")
except ValueError:
    print("escribe un numero valido")


#---------------------------------------

import os
os.system("cls")

lista=[]
rellenar(lista)
mostrar(lista)
suma(lista)
mayor(lista)
menor(lista)