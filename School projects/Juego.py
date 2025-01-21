import os

import pygame

# Incializar la librería
pygame.init()

##########   COLORES  ############
NEGRO=(0,0,0)
BLANCO=(255,255,255)
VERDE=(0,255,0)
AMARILLO=(255,255,0)
##################################

# Crearemos la ventana de trabajo

medidas = [500,500]
ventana = pygame.display.set_mode(medidas)
pygame.display.set_caption("Mi primera ventana")

# -------- Bucle principal del Programa -----------
fin=0
while fin==0:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            fin=1
    print("hola")
    ventana.fill(NEGRO)
    pygame.display.flip()

pygame.quit()