import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)

# Fontes
font_large = pygame.font.Font(None, 40)
font_small = pygame.font.Font(None, 30)

# Variáveis globais
numero_secreto = random.randint(1, 100)
tentativa = ""
mensagem = "Escolha um modo: [F] Fácil | [D] Difícil"
modo_dificil = False
acertou = False
tentativas_restantes = 5  # Usado apenas no modo difícil
escolhendo_modo = True  # Para garantir que o jogador escolha antes de jogar

# Loop do jogo
running = True

while running:

    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        elif event.type == pygame.KEYDOWN:

            if escolhendo_modo:  # Escolha do modo antes do jogo começar

                if event.key == pygame.K_f:

                    modo_dificil = False

                    mensagem = "Modo Fácil! Adivinhe um número entre 1 e 100"
                    escolhendo_modo = False

                elif event.key == pygame.K_d:

                    modo_dificil = True
                    mensagem = "Modo Difícil! Você tem 5 tentativas."
                    tentativas_restantes = 5  # Reseta tentativas
                    escolhendo_modo = False

            elif acertou:  # Se o jogador já acertou, perguntar se quer jogar de novo

                if event.key == pygame.K_y:  # Jogar novamente

                    numero_secreto = random.randint(1, 100)  # Novo número
                    tentativa = ""
                    mensagem = "Escolha um modo: [F] Fácil | [D] Difícil"
                    acertou = False
                    escolhendo_modo = True
                    
                elif event.key == pygame.K_n:  # Sair do jogo

                    running = False
            
            else:  # Jogo normal
                if event.key == pygame.K_RETURN:

                    if tentativa.isdigit():  # Verifica se é um número

                        chute = int(tentativa)

                        if chute == numero_secreto:

                            mensagem = f"🎉 Correto! O número era {numero_secreto}!"
                            acertou = True  # Ativa a opção de continuar

                        else:

                            diferenca = abs(chute - numero_secreto)

                            # Dicas baseadas na diferença

                            if diferenca > 20:

                                if chute < numero_secreto:

                                    mensagem = "Muito baixo!"

                                else:

                                    mensagem = "Muito alto!"

                            else:

                                if chute < numero_secreto:

                                    mensagem = "Muito baixo!"

                                else:

                                    mensagem =  "Muito alto!"

                            if modo_dificil:  # Se estiver no modo difícil, reduz tentativas

                                tentativas_restantes -= 1

                                if tentativas_restantes == 0:

                                    mensagem = f"Você perdeu! O número era {numero_secreto}!"
                                    acertou = True  # Para exibir a opção de reiniciar

                                else:

                                    mensagem += f" Tentativas restantes: {tentativas_restantes}"

                    else:

                        mensagem = "Digite apenas números!"
                    tentativa = ""  # Reseta a tentativa

                elif event.key == pygame.K_BACKSPACE:

                    tentativa = tentativa[:-1]  # Apaga um caractere
                
                else:

                    if event.unicode.isdigit():

                        tentativa += event.unicode  # Adiciona número à tentativa

    # Renderiza os textos
    title_text = font_large.render("Adivinhe o Número!", True, BLACK)
    input_box = font_large.render(tentativa, True, BLACK)
    message_box = font_small.render(mensagem, True, BLUE if not acertou else RED)

    # Posiciona os textos centralizados
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
    screen.blit(message_box, (WIDTH // 2 - message_box.get_width() // 2, 250))
    
    # Desenha a caixa de entrada centralizada (apenas se já escolheu o modo)
    if not escolhendo_modo:

        input_rect = pygame.Rect(WIDTH // 2 - 100, 150, 200, 50)
        pygame.draw.rect(screen, BLACK, input_rect, 2)
        screen.blit(input_box, (input_rect.x + 10, input_rect.y + 10))

    # Se acertou ou perdeu, exibe a opção de jogar novamente
    if acertou:
        
        restart_text = font_small.render("Deseja jogar novamente? (y/n)", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 300))

    pygame.display.flip()

# Encerra o pygame
pygame.quit()
