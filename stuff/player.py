import pygame
from Settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image = pygame.image.load("C:/Users/Codewiz/Documents/Dan Sidi/stuff/character.png")
        self.image = pygame.transform.scale(self.image, (100, 75))
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_HEIGHT//2, SCREEN_WIDTH//2