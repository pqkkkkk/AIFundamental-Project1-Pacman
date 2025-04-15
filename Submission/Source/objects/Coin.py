import pygame
from Global import CELL_SIZE, WHITE

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (CELL_SIZE // 2, CELL_SIZE // 2), CELL_SIZE // 6)
        self.rect = self.image.get_rect(topleft=(x, y))

    def Draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
