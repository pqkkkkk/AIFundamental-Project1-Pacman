import pygame
from objects import Coin
from objects import Ghost
from objects import Pacman
from objects import EventManager
from objects import ScoreManager
from images import *

pygame.init()
# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Objects in the game
eventManager = EventManager.EventManager()
scoreManager = ScoreManager.ScoreManager(eventManager)
coins = []
ghosts = []
pacman = Pacman.Pacman(eventManager, 0, 0, "images/Pacman.png")

# Screen dimensions
width = 900
height = 600
CELL_SIZE = 30
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Creating a map
map_width = width // CELL_SIZE
map_height = height // CELL_SIZE
map = [[1 if x == 0 or x == map_width - 1 or y == 0 or y == map_height - 1 else 0 for x in range(map_width)] for y in range(map_height)]

# Adding some coins for demonstration
map[2][2] = 2
map[3][3] = 2
# Draw coins in the map
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 2:
            coin = Coin.Coin(x * CELL_SIZE, y * CELL_SIZE)
            coins.append(coin)
for coin in coins:
    coin.Draw(screen)

# Add some ghosts
blueGhost = Ghost.Ghost(eventManager, 10 * CELL_SIZE, 10 * CELL_SIZE, "images/BlueGhost.png")
orangeGhost = Ghost.Ghost(eventManager, 11 * CELL_SIZE, 11* CELL_SIZE, "images/OrangeGhost.png")
redGhost = Ghost.Ghost(eventManager, 12* CELL_SIZE, 12 * CELL_SIZE, "images/RedGhost.png")
pinkGhost = Ghost.Ghost(eventManager, 14 * CELL_SIZE , 14 * CELL_SIZE, "images/PinkGhost.png")
ghosts.append(blueGhost)
ghosts.append(orangeGhost)
ghosts.append(redGhost)
ghosts.append(pinkGhost)
# Draw ghosts in the map
for ghost in ghosts:
    ghost.Draw(screen)

# Draw pacman in the map
pacman.Draw(screen)

# Game caption
pygame.display.set_caption("Pacman")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pacman.OnKeyDown(event)
            pacman.Update()
            screen.fill(BLACK,(pacman.olx_x,pacman.olx_y,CELL_SIZE,CELL_SIZE))
            pacman.Draw(screen)
    
    pygame.display.flip()

    clock.tick(60)
pygame.quit()