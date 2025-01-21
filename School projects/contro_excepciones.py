import os
os.system("cls")

def divide(x,y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        divide(int(input("escribe el numero 1: ")),int(input("escribe el numero 2: ")))
    except TypeError:
        print("error en la conversion de tipos")
        divide(int(input("escribe el numero 1: ")),int(input("escribe el numero 2: ")))
    else:
        print("el resultado es:",resultado)
    finally:
        print("esto se ejecutara siempre")

try:
    divide(int(input("escribe el numero 1: ")),int(input("escribe el numero 2: ")))
except ValueError:
        print("escribe un numero correcto")
        divide(int(input("escribe el numero 1: ")),int(input("escribe el numero 2: ")))

#-----------------------------------------------------------------------------------

