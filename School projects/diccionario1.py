import os
os.system("cls")


divisas = {
    "Euro": "€",
    "Dolar": "$",
    "yen": "¥",
    "Libra": "£",
}


# try:
#     #print("el simbolo del euro es:",divisas["Euro"])
#     for clave in divisas.keys():
#         print(clave)

#     for valor in divisas.values():
#         print(valor)

#     clave = str(input("Introduce un tipo de divisa: "))
#     valor = str(input("Introduce el simbolo de la divisa: "))

#     divisas.update({clave: valor})
#     print(divisas)

#     clave = str(input("Introduce un tipo de divisa a eliminar: "))
#     del divisas[clave]
#     print(divisas)

# except:
#     print("se ha producido un error")

print("Menu")
print("1. Añadir elemento")
print("2. Eliminar elemento")
print("3. imprimir diccionario")
print("4. Salir")
opcion = int(input("introduce una opcion: "))
while opcion != 4:
    if opcion == 1:
        clave = str(input("Introduce un tipo de divisa: "))
        valor = str(input("Introduce el simbolo de la divisa: "))
        divisas.update({clave: valor})
    elif opcion == 2:
        clave = str(input("Introduce un tipo de divisa a eliminar: "))
        del divisas[clave]
    elif opcion == 3:
        print(divisas)
    print("Menu")
    print("1. Añadir elemento")
    print("2. Eliminar elemento")
    print("3. imprimir diccionario")
    print("4. Salir")
    opcion = int(input("introduce una opcion: "))
