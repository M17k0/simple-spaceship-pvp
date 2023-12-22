import pygame
import os

from src.config import HEIGHT, WIDTH, BACKGROUND_IMAGE

SPACESHIP_WIDTH, SPACESHIT_HEIGHT = 60, 50
PLAYER_VELLOCITY = 5
BULLETS_VELLOCITY = 8

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship battle")

BACKGROUND = pygame.image.load(BACKGROUND_IMAGE)

PLAYER_1_IMAGE = pygame.image.load(os.path.join("Assets", "player1.png"))
PLAYER_1 = pygame.transform.rotate(pygame.transform.scale(PLAYER_1_IMAGE, (SPACESHIP_WIDTH, SPACESHIT_HEIGHT)), 270)

PLAYER_2_IMAGE = pygame.image.load(os.path.join("Assets", "player2.png"))
PLAYER_2 = pygame.transform.rotate(pygame.transform.scale(PLAYER_2_IMAGE, (SPACESHIP_WIDTH, SPACESHIT_HEIGHT)), 90)

def draw(player1, player2):
    WINDOW.fill("red")
    pygame.draw.rect(WINDOW, "black", BORDER)
    WINDOW.blit(PLAYER_1, (player1.x, player1.y))
    WINDOW.blit(PLAYER_2, (player2.x, player2.y))

    pygame.display.update()

def main():
    run = True

    player1 = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIT_HEIGHT)
    player2 = pygame.Rect(600, 300, SPACESHIP_WIDTH, SPACESHIT_HEIGHT)

    clock = pygame.time.Clock()

    bullets = []

    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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

        draw(player1, player2)

    pygame.quit()

if __name__ == "__main__":
    main()