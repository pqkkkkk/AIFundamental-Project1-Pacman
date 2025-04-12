import pygame

CELL_SIZE = 24
class Pacman(pygame.sprite.Sprite):
    def __init__(self, eventManager, x, y, image):
        super().__init__()
        self.eventManager = eventManager
        self.x = x
        self.y = y
        self.olx_x = x
        self.old_y = y
        self.avatar = pygame.image.load(image)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.image.blit(self.avatar, (0, 0))
        self.rect = self.image.get_rect(top=x, left=y)
        self.speed = 1
        self.direction = "right"

    def CheckCollisionWithWallIfMove(self,event, map):
        if event.key == pygame.K_LEFT:
            if map[int(self.x / CELL_SIZE)][int(self.y / CELL_SIZE) - 1] == 1:
                return True
        elif event.key == pygame.K_RIGHT:
            if map[int(self.x / CELL_SIZE)][int(self.y / CELL_SIZE) + 1] == 1:
                return True
        elif event.key == pygame.K_UP:
            if map[int(self.x / CELL_SIZE) - 1][int(self.y / CELL_SIZE)] == 1:
                return True
        elif event.key == pygame.K_DOWN:
            if map[int(self.x / CELL_SIZE) + 1][int(self.y / CELL_SIZE)] == 1:
                return True
        return False
    
    def OnKeyDown(self, event):
        if event.key == pygame.K_LEFT:
            self.direction = "left"
        elif event.key == pygame.K_RIGHT:
            self.direction = "right"
        elif event.key == pygame.K_UP:
            self.direction = "up"
        elif event.key == pygame.K_DOWN:
            self.direction = "down"

    def Update(self,frameCouter):
        self.olx_x = self.x
        self.olx_y = self.y

        if self.direction == "left":
            self.y -= self.speed * CELL_SIZE
        elif self.direction == "right":
            self.y += self.speed * CELL_SIZE
        elif self.direction == "up":
            self.x -= self.speed * CELL_SIZE
        elif self.direction == "down":
            self.x += self.speed * CELL_SIZE
        self.rect = pygame.Rect(self.y, self.x, CELL_SIZE, CELL_SIZE)

        data = {
            "x": self.x,
            "y": self.y,
            "frameCounter": frameCouter,
        }
        self.eventManager.publish("PACMAN_MOVED", data)