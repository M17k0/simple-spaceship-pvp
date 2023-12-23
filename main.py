import pygame

from src.config import PLAYER_1_IMAGE, PLAYER_2_IMAGE, SPACESHIP_WIDTH, SPACESHIT_HEIGHT, FPS
from src.config import INITIAL_X_P1, INITIAL_Y_P1, INITIAL_X_P2, INITIAL_Y_P2
from src.player import Player
from src.screen import draw_screen, draw_winner

def main():
    player1 = Player(INITIAL_X_P1, INITIAL_Y_P1, SPACESHIP_WIDTH, SPACESHIT_HEIGHT, PLAYER_1_IMAGE, 270, 1)
    player2 = Player(INITIAL_X_P2, INITIAL_Y_P2, SPACESHIP_WIDTH, SPACESHIT_HEIGHT, PLAYER_2_IMAGE, 90, 2)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.add_bullets()
                if event.key == pygame.K_RCTRL:
                    player2.add_bullets()

            if event.type == pygame.USEREVENT + 2:
                player1.get_hit()
            if event.type == pygame.USEREVENT + 1:
                player2.get_hit()

        keys = pygame.key.get_pressed()
        Player.handle_movement(player1, player2, keys)

        Player.handle_bullets(player1, player2)

        draw_screen(player1, player2)

        if player1.health <= 0:
            draw_winner("Player 2 WINS")
            run = False
        if player2.health <= 0:
            draw_winner("Player 1 WINS")
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()