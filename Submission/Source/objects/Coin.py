import pygame
CELL_SIZE = 24
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.avatar = pygame.image.load("images/Coin.png")
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.image.blit(self.avatar, (0, 0))
        self.rect = self.image.get_rect(top=x, left=y)

    
    def Draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
        