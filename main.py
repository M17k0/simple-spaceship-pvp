import pygame
import os
pygame.font.init()

from src.config import HEIGHT, WIDTH, BACKGROUND_IMAGE

SPACESHIP_WIDTH, SPACESHIT_HEIGHT = 60, 50
PLAYER_VELLOCITY = 5
BULLETS_VELLOCITY = 8
MAX_BULLETS = 3

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship battle")

BACKGROUND = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("arial", 40)

PLAYER_1_IMAGE = pygame.image.load(os.path.join("Assets", "player1.png"))
PLAYER_1 = pygame.transform.rotate(pygame.transform.scale(PLAYER_1_IMAGE, (SPACESHIP_WIDTH, SPACESHIT_HEIGHT)), 270)

PLAYER_2_IMAGE = pygame.image.load(os.path.join("Assets", "player2.png"))
PLAYER_2 = pygame.transform.rotate(pygame.transform.scale(PLAYER_2_IMAGE, (SPACESHIP_WIDTH, SPACESHIT_HEIGHT)), 90)

def draw(player1, player2, p1_bullets, p2_bullets, p1_health, p2_health):
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WINDOW, "black", BORDER)

    p1_health_text = FONT.render(f"HEALTH: {p1_health}", 1, "white")
    p2_health_text = FONT.render(f"HEALTH: {p2_health}", 1, "white")
    WINDOW.blit(p1_health_text, (10, 10))
    WINDOW.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))

    WINDOW.blit(PLAYER_1, (player1.x, player1.y))
    WINDOW.blit(PLAYER_2, (player2.x, player2.y))

    for bullet in p1_bullets:
        pygame.draw.rect(WINDOW, "white", bullet)

    for bullet in p2_bullets:
        pygame.draw.rect(WINDOW, "yellow", bullet)

    pygame.display.update()

PLAYER_1_HIT = pygame.USEREVENT + 1
PLAYER_2_HIT = pygame.USEREVENT + 2

def handle_bullets(p1_bullets, p2_bullets, p1, p2):
    for bullet in p1_bullets:
        bullet.x += BULLETS_VELLOCITY

        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_2_HIT))
            p1_bullets.remove(bullet)
        if bullet.x > WIDTH:
            p1_bullets.remove(bullet)

    for bullet in p2_bullets:
        bullet.x -= BULLETS_VELLOCITY

        if p1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_1_HIT))
            p2_bullets.remove(bullet)
        if bullet.x <= 0:
            p2_bullets.remove(bullet)
        
def draw_winner(text):
    draw_text = FONT.render(text, 1, "white")
    WINDOW.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5_000)

def main():
    run = True

    player1 = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIT_HEIGHT)
    player2 = pygame.Rect(600, 300, SPACESHIP_WIDTH, SPACESHIT_HEIGHT)

    clock = pygame.time.Clock()

    player1_bullets = []
    player2_bullets = []


    p1_health = p2_health = 10

    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(player1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player1.x + player1.width, player1.y + player1.height // 2 - 2, 10, 5)
                    player1_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(player2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player2.x, player2.y + player2.height // 2 - 2, 10, 5)
                    player2_bullets.append(bullet)
            
            if event.type == PLAYER_1_HIT:
                p1_health -= 1
            if event.type == PLAYER_2_HIT:
                p2_health -= 1

        winner_text = ""
        if p1_health <= 0:
            winner_text = "P2 WINS"
        if p2_health <= 0:
            winner_text = "P1 WINS"
        if winner_text != "":
            draw_winner(winner_text)
            run = False
            break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x - PLAYER_VELLOCITY > 0 :
            player1.x -= PLAYER_VELLOCITY
        if keys[pygame.K_d] and player1.x + PLAYER_VELLOCITY + player1.width < BORDER.x:
            player1.x += PLAYER_VELLOCITY
        if keys[pygame.K_s] and player1.y + PLAYER_VELLOCITY + player1.height < HEIGHT:
            player1.y += PLAYER_VELLOCITY
        if keys[pygame.K_w] and player1.y - PLAYER_VELLOCITY > 0:
            player1.y -= PLAYER_VELLOCITY
        
        if keys[pygame.K_LEFT] and player2.x - PLAYER_VELLOCITY > BORDER.x + BORDER.width:
            player2.x -= PLAYER_VELLOCITY
        if keys[pygame.K_RIGHT] and player2.x + PLAYER_VELLOCITY + player2.width < WIDTH:
            player2.x += PLAYER_VELLOCITY
        if keys[pygame.K_DOWN] and player2.y + PLAYER_VELLOCITY + player2.height < HEIGHT:
            player2.y += PLAYER_VELLOCITY
        if keys[pygame.K_UP] and player2.y - PLAYER_VELLOCITY > 0:
            player2.y -= PLAYER_VELLOCITY

        handle_bullets(player1_bullets, player2_bullets, player1, player2)

        draw(player1, player2, player1_bullets, player2_bullets, p1_health, p2_health)

    pygame.quit()

if __name__ == "__main__":
    main()