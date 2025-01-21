# Fecha: 28 de noviembre de 2024
# Programador: Sergi
# Descripcion: Este programa creara una lista con las 10 comidas favoritas del usuario

import os

os.system("cls")

comida=[]
for i in range(5):
    comida.append(input("dime tu comidas favorita: "))
print(comida)