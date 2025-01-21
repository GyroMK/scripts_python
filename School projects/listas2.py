# Fecha: 28 de noviembre de 2024
# Programador: Sergi
# Descripcion: Este programa utilizara listas

import os

os.system("cls")

alumno = ["Pepe","Garcia","Muñoz",34,"Hombre"]

print("Estos son los datos del alumno:",alumno)
print("Estos son los datos del alumno:")
print("Nombre:",alumno[0])
print("Apellido1:",alumno[1])
print("Apellido2:",alumno[2])
print("edad:",alumno[3])
print("sexo:",alumno[4])

#añadir elementos a la lista
alumno.append(175)
print("altura:", alumno[5])

alumno.insert(3, "75kg")
print(alumno)

pos=int(input("dime la posicion: "))
valor=str(input("dime el valor a poner en esa posicion: "))

alumno.insert(pos, valor)
print(alumno)

