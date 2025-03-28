import pygame

CELL_SIZE = 24
class Ghost(pygame.sprite.Sprite):
    def __init__(self,eventManager,x,y,image):
        super().__init__()
        self.x = x
        self.y = y
        self.avatar = pygame.image.load(image)
        self.eventManager = eventManager
        eventManager.subscribe("PACMAN_MOVED",self.OnPacmanMoved)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.image.blit(self.avatar, (0, 0))
        self.rect = self.image.get_rect(top=x, left=y)    
    def OnPacmanMoved(self, data):
        pass
        