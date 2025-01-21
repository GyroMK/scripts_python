# Fecha: 21 de noviembre de 2024
# Programador: Sergi
# Descripcion: Programa para calcular el mayor de dos numeros
import os

os.system("cls")

num1=int(input("Escribe el primer numero: "))
num2=int(input("Escribe el segundo numero: "))

if num1>num2:
    print(num1, "es el mayor")
elif num2==num1:
    print(num1,"y",num2,"son iguales")
else:
    print(num2, "es el mayor")
