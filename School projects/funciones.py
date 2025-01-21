# descripcion: iniciacion a las funciones
# fecha: 9 de enero
# Autor:Sergi

import os

os.system("cls")

# crearemos una funcion llamada saludo que imprimira un mensaje

"""def saludo():
    print("Hola que tal estas.")

print("Este es el inicio del programa")
saludo()
print("Este es el final del programa")"""

# crearemos una funcion que sume dos numeros

'''def suma():
    primer = int(input("Escribe el primer numero:\n"))
    segundo = int(input("Escribe el segundo numero:\n"))
    print("el resultado es: ", primer + segundo)

suma()'''

# funcion que reciba 2 parametros como numeros y los sume

'''def suma(num1=0,num2=0):
    print("la suma de los numeros es:",num1+num2)

suma(3,3)'''

def mayor(num1,num2):
    if num1 > num2:
        print("el mayor es",num1)
    else:
        print("el mayor es",num2)

mayor(num1=input("Escibe un numero:\n"),num2=input("Escibe otro numero:\n"))