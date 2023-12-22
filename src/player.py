import pygame

from .config import HEIGHT, WIDTH

class Player:
    MAX_BULLETS = 3
    PLAYER_VELLOCITY = 5
    BULLETS_VELLOCITY = 8
    def __init__(self, x, y, width, height, image_path, rotate_angle):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(image_path), (width, height)), rotate_angle)
        self.bullets = []
        self.health = 10
    
    def draw_player(self, screen):
        screen.blit(self.image, self.rect)

    def handle_movement(self, keys, player):
        if player == 1:
            if keys[pygame.K_a] and self.rect.x - Player.PLAYER_VELLOCITY > 0 :
                self.rect.x -= Player.PLAYER_VELLOCITY
            if keys[pygame.K_d] and self.rect.x + Player.PLAYER_VELLOCITY + self.rect.width < WIDTH // 2 - 5:
                self.rect.x += Player.PLAYER_VELLOCITY
            if keys[pygame.K_s] and self.rect.y + Player.PLAYER_VELLOCITY + self.rect.height < HEIGHT:
                self.rect.y += Player.PLAYER_VELLOCITY
            if keys[pygame.K_w] and self.rect.y - Player.PLAYER_VELLOCITY > 0:
                self.rect.y -= Player.PLAYER_VELLOCITY
        else:
            if keys[pygame.K_LEFT] and self.rect.x - Player.PLAYER_VELLOCITY > WIDTH // 2 - 5 + 10:
                self.rect.x -= Player.PLAYER_VELLOCITY
            if keys[pygame.K_RIGHT] and self.rect.x + Player.PLAYER_VELLOCITY + self.rect.width < WIDTH:
                self.rect.x += Player.PLAYER_VELLOCITY
            if keys[pygame.K_DOWN] and self.rect.y + Player.PLAYER_VELLOCITY + self.rect.height < HEIGHT:
                self.rect.y += Player.PLAYER_VELLOCITY
            if keys[pygame.K_UP] and self.rect.y - Player.PLAYER_VELLOCITY > 0:
                self.rect.y -= Player.PLAYER_VELLOCITY

    def add_bullets(self, player):
        if player == 1:
            bullet = pygame.Rect(self.rect.x + self.rect.width, self.rect.y + self.rect.height // 2 - 2, 10, 5)
        else:
            bullet = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2 - 2, 10, 5)
        
        if len(self.bullets) < 3:
            self.bullets.append(bullet)

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            pygame.draw.rect(screen, "white", bullet)