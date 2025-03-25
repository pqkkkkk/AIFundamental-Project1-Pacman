import pygame
class Ghost():
    def __init__(self,eventManager,x,y,image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.eventManager = eventManager
        eventManager.subscribe("PACMAN_MOVED",self.OnPacmanMoved)
    
    def Draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
    
    def OnPacmanMoved(self, data):
        pass
        