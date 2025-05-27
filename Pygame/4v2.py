import pygame
import sys
import subprocess
import tempfile
import random
import string
import os

# Inicializar o Pygame
pygame.init()

# Configurações da tela principal
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu do Jogo')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARKGRAY = (100, 100, 100)

# Fonte
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def show_popup(message, title="Créditos"):
    popup_width, popup_height = 400, 200
    popup_surface = pygame.Surface((popup_width, popup_height))
    popup_surface.fill(DARKGRAY)
    
    # Cria uma nova tela para desenhar o pop-up sobre a tela principal
    popup_rect = pygame.Rect((screen_width - popup_width) // 2, (screen_height - popup_height) // 2, popup_width, popup_height)
    screen.blit(popup_surface, popup_rect.topleft)
    
    draw_text(title, font, WHITE, popup_surface, popup_width // 2, 40)
    draw_text(message, small_font, WHITE, popup_surface, popup_width // 2, popup_height // 2)
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
                break

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_button.collidepoint(x, y):
                    iniciar_jogo()
                elif credits_button.collidepoint(x, y):
                    mostrar_creditos()
                elif exit_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)

        # Desenhar o menu
        draw_text('Menu do Jogo', font, BLACK, screen, screen_width // 2, 100)
                
        start_button = pygame.draw.rect(screen, GRAY, (300, 200, 200, 50))
        draw_text('Iniciar', small_font, BLACK, screen, screen_width // 2, 225)
        
        credits_button = pygame.draw.rect(screen, GRAY, (300, 300, 200, 50))
        draw_text('Créditos', small_font, BLACK, screen, screen_width // 2, 325)
        
        exit_button = pygame.draw.rect(screen, GRAY, (300, 400, 200, 50))
        draw_text('Sair', small_font, BLACK, screen, screen_width // 2, 425)

        pygame.display.flip()

def iniciar_jogo():
    pygame.quit()
    subprocess.Popen(["python", "Pygame\\5.py"])
    sys.exit()

def mostrar_creditos():
    pygame.quit()

    # Gera um nome aleatório
    nome_arquivo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    caminho_temp = os.path.join(tempfile.gettempdir(), f"creditos_{nome_arquivo}.py")

    conteudo_creditos = '''import pygame
import sys
import subprocess

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Créditos")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main():
    running = True
    while running:
        screen.fill(WHITE)

        draw_text("Créditos", font, BLACK, screen, screen_width // 2, 80)
        draw_text("Rian", small_font, BLACK, screen, screen_width // 2, 180)
        draw_text("Wendel", small_font, BLACK, screen, screen_width // 2, 230)
        draw_text("Chat GPT", small_font, BLACK, screen, screen_width // 2, 280)
        draw_text("Escola SESI SENAI", small_font, BLACK, screen, screen_width // 2, 330)

        voltar_button = pygame.draw.rect(screen, GRAY, (300, 450, 200, 50))
        draw_text("Voltar", small_font, BLACK, screen, screen_width // 2, 475)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if voltar_button.collidepoint(x, y):
                    running = False

        pygame.display.flip()

    pygame.quit()
    subprocess.Popen(["python", "Pygame\\\\4v2.py"])
    sys.exit()

if __name__ == "__main__":
    main()
'''

    with open(caminho_temp, "w", encoding="utf-8") as f:
        f.write(conteudo_creditos)

    subprocess.Popen(["python", caminho_temp])
    sys.exit()

if __name__ == "__main__":
    main_menu()
