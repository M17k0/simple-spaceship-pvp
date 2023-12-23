import os

FPS = 60

HEIGHT = 500
WIDTH = 900

SPACESHIP_WIDTH = 60
SPACESHIT_HEIGHT =  50

BACKGROUND_IMAGE = os.path.join("assets", "background.png")
PLAYER_1_IMAGE = os.path.join("assets", "player1.png")
PLAYER_2_IMAGE = os.path.join("assets", "player2.png")

INITIAL_X_P1 = WIDTH // 2 - WIDTH // 4
INITIAL_Y_P1 = HEIGHT // 2 

INITIAL_X_P2 = WIDTH // 2 + WIDTH //4
INITIAL_Y_P2 = HEIGHT // 2

BULLET_FIRE_MP3 = os.path.join("assets", "fire.mp3")
BULLET_HIT_MP3 = os.path.join("assets", "hit.mp3")