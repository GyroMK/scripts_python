import pygame
import random
import sys
from tkinter import Tk, filedialog, simpledialog

# Configuración inicial
pygame.init()

# Constantes
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Juego de Rompecabezas")

class PuzzlePiece:
    def __init__(self, image, correct_pos, current_pos, tolerance=50):  # Tolerancia aumentada a 50
        self.image = image
        self.correct_pos = correct_pos
        self.current_pos = current_pos
        self.rect = self.image.get_rect(topleft=current_pos)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.correct = False  # Nueva variable para saber si la pieza está en su lugar
        self.tolerance = tolerance  # Radio de tolerancia

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def handle_event(self, event, pieces):
        if self.correct:  # Si la pieza ya está en su lugar, no hacer nada
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not any(piece.dragging for piece in pieces):
                self.dragging = True
                self.offset_x = event.pos[0] - self.rect.x
                self.offset_y = event.pos[1] - self.rect.y
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            # Verificar si la pieza está dentro del radio de tolerancia de la posición correcta
            if self.is_in_place():
                self.rect.topleft = self.correct_pos  # Ajuste a la posición correcta
                self.correct = True  # Marcar la pieza como correcta
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.rect.x = event.pos[0] - self.offset_x
            self.rect.y = event.pos[1] - self.offset_y

    def is_in_place(self):
        # Comprobar si la pieza está dentro del radio de tolerancia de la posición correcta
        rect_center = pygame.math.Vector2(self.rect.centerx, self.rect.centery)
        correct_center = pygame.math.Vector2(self.correct_pos[0] + self.rect.width / 2, self.correct_pos[1] + self.rect.height / 2)
        
        distance = rect_center.distance_to(correct_center)
        return distance < self.tolerance  # Devolver True si la pieza está cerca de su posición correcta

def split_image(image, rows, cols):
    piece_width = image.get_width() // cols
    piece_height = image.get_height() // rows
    pieces = []
    positions = []
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * piece_width, row * piece_height, piece_width, piece_height)
            piece = image.subsurface(rect).copy()
            correct_pos = (col * piece_width, row * piece_height)
            positions.append(correct_pos)
            pieces.append(PuzzlePiece(piece, correct_pos, correct_pos))
    random.shuffle(positions)
    for i, piece in enumerate(pieces):
        piece.current_pos = positions[i]
        piece.rect.topleft = positions[i]
    return pieces

def check_win(pieces):
    # Comprobar si todas las piezas están en su lugar
    return all(piece.correct for piece in pieces)

def main():
    clock = pygame.time.Clock()
    
    # Selección de imagen mediante diálogo de archivo
    Tk().withdraw()  # Ocultar ventana de Tkinter
    file_path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imagenes", "*.jpg;*.png;*.bmp")])
    if not file_path:
        print("No se seleccionó ninguna imagen. Cerrando programa.")
        pygame.quit()
        sys.exit()
    
    image = pygame.image.load(file_path)
    image = pygame.transform.scale(image, (display_width, display_height))

    # Pedir el número de piezas del rompecabezas
    rows = simpledialog.askinteger("Filas", "Introduce el número de filas:", minvalue=2, maxvalue=10)
    cols = simpledialog.askinteger("Columnas", "Introduce el número de columnas:", minvalue=2, maxvalue=10)
    
    if not rows or not cols:
        print("No se introdujo un número válido de filas o columnas. Cerrando programa.")
        pygame.quit()
        sys.exit()
    
    pieces = split_image(image, rows, cols)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for piece in pieces:
                piece.handle_event(event, pieces)

        for piece in pieces:
            piece.draw(screen)

        # Verificar si se ha ganado
        if check_win(pieces):
            font = pygame.font.SysFont("Arial", 36)
            text = font.render("¡Ganaste!", True, (0, 255, 0))
            screen.blit(text, (display_width // 2 - text.get_width() // 2, display_height // 2 - text.get_height() // 2))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
