 # programa que crea nuestra primera clase
 # fecha: 11/2/2025
import os

os.system('cls')

class coches:
    def __init__(self,c,m,p):
        self.color = c
        self.marca = m
        self.num_puertas = p

    def arrancar(self):
        print("el coche ha sido arrancado")

    def parar(self):
        print("el coche ha sido parado")

    def cambia_color(self, nuevo_color):
        self.color = nuevo_color
        print('el nuevo color es:', self.color)

# creamos un objeto sobre esa clase

leon=coches('negro','seat',5)
laferrari=coches('rojo','ferrari',3)

print("el color del ferrari es", laferrari.color)

leon.arrancar()

# cambiamos el color de leon
leon.cambia_color(input('introduce el nuevo color'))