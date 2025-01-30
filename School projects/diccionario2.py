import os
os.system("cls")

# notas = {}
# for i in range(5):
#     asignatura=str(input("Introduce la asignatura: "))
#     nota=int(input("Introduce la nota: "))
#     notas.update({asignatura:nota})

# for nota in notas.items():
#     print("la asignatura", nota[0], "tiene una nota de", nota[1])
# mayor = 11
# for notaMayor in notas.items():
#     if notaMayor[1] < mayor:
#         mayor = notaMayor[1]
#         asignatura = notaMayor[0]
# print("Y la nota mas baja es:",mayor, "de", asignatura)


#---------------------------------------------

alumnos = {}
Continuar = "S"

while Continuar == "S":
    nombre = str(input("Introduce el nombre del alumno: "))
    edad = int(input("Introduce la edad del alumno: "))
    alumnos.update({nombre:edad})
    print("Alumno añadido")
    continuar = input("¿Quieres añadir más alumnos? (S/N): ")
    if continuar == "N" or continuar == "n":
        break
for alumno, edad in alumnos.items():
    print("El alumno", alumno, "tiene", edad, "años")