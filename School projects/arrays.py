# Fecha: 26 de noviembre de 2024
# Programador: Sergi
# Descripcion: Este programa utilizara listas

import os

os.system ("cls")

#numeros = [10,56,34,21,8]

"""print("esta es nuestra lista: ", numeros)

print("este es el tercer elemento: ", numeros[2])
print("este es el primer elemento: ", numeros[0])

# cambiar el valor de un numero
numeros[3] = 44
print("este es el cuarto elemento: ", numeros[3])

num = int(input("Escribe un numero para poner en la posicion 3: "))
numeros[2] = num
print(numeros)"""

###################################################
#
# Mediante el uso de for, rellenar una lista de 5 numeros
#
###################################################
var=5
numeros=[None]*var
for i in range(var):
    numeros[i]= int(input("escribe un numero: "))
print(numeros)