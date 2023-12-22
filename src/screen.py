import pygame

from .config import HEIGHT, WIDTH, BACKGROUND_IMAGE

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship battle")

BACKGROUND = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), (WIDTH, HEIGHT))

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

FONT = pygame.font.SysFont("arial", 40)

MIDDLE_Y_P1 = BORDER.x // 2 
MIDDLE_X_P1 = HEIGHT // 2

MIDDLE_Y_P2 = BORDER.x + BORDER.x // 2 
MIDDLE_X_P2 = HEIGHT // 2

def draw_screen(player1, player2):
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WINDOW, "black", BORDER)

    p1_health_text = FONT.render(f"HEALTH: {player1.health}", 1, "white")
    p2_health_text = FONT.render(f"HEALTH: {player2.health}", 1, "white")
    WINDOW.blit(p1_health_text, (10, 10))
    WINDOW.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))

    player1.draw_player(WINDOW)
    player2.draw_player(WINDOW)
    
    player1.draw_bullets(WINDOW)
    player2.draw_bullets(WINDOW)

    pygame.display.update()

def draw_winner(text):
    draw_text = FONT.render(text, 1, "white")
    WINDOW.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5_000)