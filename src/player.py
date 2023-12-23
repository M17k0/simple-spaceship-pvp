import pygame

from .config import HEIGHT, WIDTH
from .screen import BORDER
from src.config import BULLET_FIRE_MP3, BULLET_HIT_MP3 

BULLET_FIRE_SOUND = pygame.mixer.Sound(BULLET_FIRE_MP3)
BULLET_HIT_SOUND = pygame.mixer.Sound(BULLET_HIT_MP3)

class Player:
    MAX_BULLETS = 3
    PLAYER_VELLOCITY = 5
    BULLETS_VELLOCITY = 8
    
    def __init__(self, x, y, width, height, image_path, rotate_angle, player_number):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(image_path), (width, height)), rotate_angle)
        self.bullets = []
        self.health = 10
        self.player_number = player_number
    
    def draw_player(self, screen):
        screen.blit(self.image, self.rect)

    def add_bullets(self):
        if self.player_number == 1 and len(self.bullets) < 3:
            bullet = pygame.Rect(self.rect.x + self.rect.width, self.rect.y + self.rect.height // 2 - 2, 10, 5)
            BULLET_FIRE_SOUND.play()
            self.bullets.append(bullet)
        elif self.player_number == 2 and len(self.bullets) < 3:
            bullet = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2 - 2, 10, 5)
            BULLET_FIRE_SOUND.play()
            self.bullets.append(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            pygame.draw.rect(screen, "white", bullet)

    def get_hit(self):
        BULLET_HIT_SOUND.play()
        self.health -= 1

    @staticmethod
    def handle_movement(player1, player2, keys):
        if keys[pygame.K_a] and player1.rect.x - Player.PLAYER_VELLOCITY > 0 :
            player1.rect.x -= Player.PLAYER_VELLOCITY
        if keys[pygame.K_d] and player1.rect.x + Player.PLAYER_VELLOCITY + player1.rect.width < BORDER.x:
            player1.rect.x += Player.PLAYER_VELLOCITY
        if keys[pygame.K_s] and player1.rect.y + Player.PLAYER_VELLOCITY + player1.rect.height < HEIGHT:
            player1.rect.y += Player.PLAYER_VELLOCITY
        if keys[pygame.K_w] and player1.rect.y - Player.PLAYER_VELLOCITY > 0:
            player1.rect.y -= Player.PLAYER_VELLOCITY

        if keys[pygame.K_LEFT] and player2.rect.x - Player.PLAYER_VELLOCITY > BORDER.x + BORDER.width:
            player2.rect.x -= Player.PLAYER_VELLOCITY
        if keys[pygame.K_RIGHT] and player2.rect.x + Player.PLAYER_VELLOCITY + player2.rect.width < WIDTH:
            player2.rect.x += Player.PLAYER_VELLOCITY
        if keys[pygame.K_DOWN] and player2.rect.y + Player.PLAYER_VELLOCITY + player2.rect.height < HEIGHT:
            player2.rect.y += Player.PLAYER_VELLOCITY
        if keys[pygame.K_UP] and player2.rect.y - Player.PLAYER_VELLOCITY > 0:
            player2.rect.y -= Player.PLAYER_VELLOCITY

    @staticmethod
    def handle_bullets(player1, player2):
        for bullet in player1.bullets:
            bullet.x += Player.BULLETS_VELLOCITY

            if player2.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))
                player1.bullets.remove(bullet)
            if bullet.x > WIDTH:
                player1.bullets.remove(bullet)

        for bullet in player2.bullets:
            bullet.x -= Player.BULLETS_VELLOCITY

            if player1.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT + 2))
                player2.bullets.remove(bullet)
            if bullet.x <= 0:
                player2.bullets.remove(bullet)