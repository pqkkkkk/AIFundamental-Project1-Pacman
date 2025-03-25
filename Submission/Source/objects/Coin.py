import pygame
class Coin:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Coin.png")
    
    def Draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
        