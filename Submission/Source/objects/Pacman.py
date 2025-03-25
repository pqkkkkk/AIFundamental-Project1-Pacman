import pygame

CELL_SIZE = 30
class Pacman():
    def __init__(self, eventManager, x, y, image):
        self.eventManager = eventManager
        self.x = x
        self.y = y
        self.olx_x = x
        self.old_y = y
        self.image = pygame.image.load(image)
        self.speed = 1
        self.direction = "right"
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def Draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def OnKeyDown(self, event):
        if event.key == pygame.K_LEFT:
            self.direction = "left"
        elif event.key == pygame.K_RIGHT:
            self.direction = "right"
        elif event.key == pygame.K_UP:
            self.direction = "up"
        elif event.key == pygame.K_DOWN:
            self.direction = "down"

    def Update(self):
        self.olx_x = self.x
        self.olx_y = self.y

        if self.direction == "left":
            self.x -= self.speed * CELL_SIZE
        elif self.direction == "right":
            self.x += self.speed * CELL_SIZE
        elif self.direction == "up":
            self.y -= self.speed * CELL_SIZE
        elif self.direction == "down":
            self.y += self.speed * CELL_SIZE
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)