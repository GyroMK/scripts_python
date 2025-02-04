import pygame
import random
import sys
from tkinter import Tk, filedialog

# Configuración básica
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
COLUMNS, ROWS = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
PANEL_WIDTH = 150

# Inicializar Pygame y la pantalla
pygame.init()
screen = pygame.display.set_mode((WIDTH + PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Personalizado")
clock = pygame.time.Clock()
pygame.key.set_repeat(100, 100)



# Cargar imágenes personalizadas para las piezas
IMAGES = [pygame.image.load(f'block_{i}.png') for i in range(7)]
IMAGES = [pygame.transform.scale(img, (GRID_SIZE, GRID_SIZE)) for img in IMAGES]

# Formas de las piezas
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

NEXT_PIECE_POSITIONS = {
    0: (20, 30),  # I
    1: (40, 40),  # O
    2: (30, 40),  # T
    3: (30, 40),  # Z
    4: (30, 40),  # S
    5: (30, 40),  # L
    6: (30, 40)   # J
}

class Piece:
    def __init__(self, x, y, shape, image, index):
        self.x, self.y = float(x), float(y)
        self.shape = shape
        self.image = image
        self.index = index

    def rotate(self, board):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.image = pygame.transform.rotate(self.image, -90)
        if check_collision(board, self):
            self.shape = [list(row) for row in zip(*self.shape)][::-1]  # Revertir rotación
            self.image = pygame.transform.rotate(self.image, 90)  # Revertir rotación de la imagen

def check_collision(board, piece, offset_x=0, offset_y=0):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell and (int(piece.y + y + offset_y) >= ROWS or int(piece.x + x + offset_x) < 0 or int(piece.x + x + offset_x) >= COLUMNS or board[int(piece.y + y + offset_y)][int(piece.x + x + offset_x)]):
                return True
    return False

def merge_piece(board, piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                board[int(piece.y + y)][int(piece.x + x)] = piece.image

def clear_lines(board):
    lines_cleared = 0
    new_board = []
    for row in board:
        if all(cell is not None for cell in row):
            lines_cleared += 1
        else:
            new_board.append(row)
    for _ in range(lines_cleared):
        new_board.insert(0, [None] * COLUMNS)
    board[:] = new_board
    return lines_cleared

def new_piece():
    index = random.randint(0, len(SHAPES) - 1)
    return Piece(COLUMNS // 2 - 1, 0, SHAPES[index], IMAGES[index], index)

def draw_board(screen, board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                screen.blit(cell, (x * GRID_SIZE, y * GRID_SIZE))

def draw_panel(screen, next_piece, score):
    pygame.draw.line(screen, (255, 255, 255), (WIDTH, 0), (WIDTH, HEIGHT), 2)
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH + 10, 10, PANEL_WIDTH - 20, 100), 2)
    
    font = pygame.font.SysFont(None, 25)
    text = font.render("Siguiente", True, (255, 255, 255))
    screen.blit(text, (WIDTH + 40, 20))
    
    offset_x, offset_y = NEXT_PIECE_POSITIONS[next_piece.index]
    
    for y, row in enumerate(next_piece.shape):
        for x, cell in enumerate(row):
            if cell:
                screen.blit(next_piece.image, (WIDTH + offset_x + x * GRID_SIZE, offset_y + y * GRID_SIZE))
    
    score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH + 25, 150))

def main_menu():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.stop
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 60)
        title_text = font.render("Tetris", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        # Botones
        font_small = pygame.font.SysFont(None, 40)
        play_text = font_small.render("Jugar", True, (255, 255, 255))
        options_text = font_small.render("Opciones", True, (255, 255, 255))
        quit_text = font_small.render("Salir", True, (255, 255, 255))

        play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        options_rect = options_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))

        screen.blit(play_text, play_rect)
        screen.blit(options_text, options_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    main_game()
                elif options_rect.collidepoint(event.pos):
                    options_menu()
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def options_menu():
    selected_piece = 0
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 40)
        title_text = font.render("Opciones", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))

        # Mostrar la pieza seleccionada
        piece_name = ["I", "O", "T", "Z", "S", "L", "J"][selected_piece]
        piece_text = font.render(f"Pieza: {piece_name}", True, (255, 255, 255))
        screen.blit(piece_text, (WIDTH // 2 - piece_text.get_width() // 2, 80))

        # Vista previa de la textura
        preview_surface = pygame.Surface((GRID_SIZE * 4, GRID_SIZE * 4))
        preview_surface.fill((50, 50, 50))
        for y, row in enumerate(SHAPES[selected_piece]):
            for x, cell in enumerate(row):
                if cell:
                    preview_surface.blit(IMAGES[selected_piece], (x * GRID_SIZE, y * GRID_SIZE))
        screen.blit(preview_surface, (WIDTH // 2 - preview_surface.get_width() // 2, 130))

        # Botones
        change_texture_text = font.render("Cambiar Textura", True, (255, 255, 255))
        back_text = font.render("Volver", True, (255, 255, 255))
        change_rect = change_texture_text.get_rect(center=(WIDTH // 2, HEIGHT - 120))
        back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        screen.blit(change_texture_text, change_rect)
        screen.blit(back_text, back_rect)

        # Flechas para navegar entre piezas
        left_arrow = pygame.Rect((WIDTH // 2 - 100, 85, 30, 30))
        right_arrow = pygame.Rect((WIDTH // 2 + 70, 85, 30, 30))
        pygame.draw.polygon(screen, (255, 255, 255), [(left_arrow.x + 25, left_arrow.y), (left_arrow.x, left_arrow.y + 15), (left_arrow.x + 25, left_arrow.y + 30)])
        pygame.draw.polygon(screen, (255, 255, 255), [(right_arrow.x, right_arrow.y), (right_arrow.x + 25, right_arrow.y + 15), (right_arrow.x, right_arrow.y + 30)])

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.collidepoint(event.pos):
                    selected_piece = (selected_piece - 1) % len(SHAPES)
                elif right_arrow.collidepoint(event.pos):
                    selected_piece = (selected_piece + 1) % len(SHAPES)
                elif change_rect.collidepoint(event.pos):
                    # Cambiar textura
                    Tk().withdraw()  # Ocultar ventana raíz de Tkinter
                    file_path = filedialog.askopenfilename(filetypes=[("Imagen PNG", "*.png")])
                    if file_path:
                        new_image = pygame.image.load(file_path)
                        new_image = pygame.transform.scale(new_image, (GRID_SIZE, GRID_SIZE))
                        IMAGES[selected_piece] = new_image
                elif back_rect.collidepoint(event.pos):
                    return

def main_game():
    pygame.mixer.init()
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)

    board = [[None] * COLUMNS for _ in range(ROWS)]
    piece = new_piece()
    next_piece = new_piece()
    running, fall_time = True, 0
    score = 0
    fall_speed = 80  # Milisegundos

    while running:
        screen.fill((0, 0, 0))
        draw_board(screen, board)
        draw_panel(screen, next_piece, score)

        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    screen.blit(piece.image, ((int(piece.x) + x) * GRID_SIZE, (int(piece.y) + y) * GRID_SIZE))
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not check_collision(board, piece, -1):
            piece.x -= 0.3
            if piece.x < 0:
                piece.x = 0
        if keys[pygame.K_RIGHT] and not check_collision(board, piece, 1):
            piece.x += 0.3
            if piece.x + len(piece.shape[0]) > COLUMNS:
                piece.x = COLUMNS - len(piece.shape[0])
        if keys[pygame.K_DOWN] and not check_collision(board, piece, 0, 1):
            piece.y += 0.3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    piece.rotate(board)
                    if check_collision(board, piece):
                        # Revertir rotación
                        piece.rotate(board)
                        piece.rotate(board)
                        piece.rotate(board)
                elif event.key == pygame.K_ESCAPE:  # Añadido para volver al menú
                    running = False
                    main_menu()

        fall_time += clock.get_rawtime()
        if fall_time > fall_speed:
            if not check_collision(board, piece, 0, 1):
                piece.y += 1
            else:
                merge_piece(board, piece)
                score += clear_lines(board) * 100
                piece = next_piece
                next_piece = new_piece()
                if check_collision(board, piece):
                    running = False  # Fin del juego
            fall_time = 0

        clock.tick(60)

def main():
    main_menu()

if __name__ == "__main__":
    main()

