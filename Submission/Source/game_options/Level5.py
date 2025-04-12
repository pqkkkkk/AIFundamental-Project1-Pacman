import pygame
from objects import Coin
from objects import Ghost
from objects import Pacman
from objects import EventManager
from objects import ScoreManager
from images import *
import os
from Global import WIDTH, HEIGHT, CELL_SIZE, RED, CreateBackground, game_map, PACMAN_POSITION

def RunGameOfLevel5():
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    os.chdir(source_dir)
    
    pygame.init()
    
    # Screen settings
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")
    
    # Background
    background = CreateBackground()
    # Create objects
    eventManager = EventManager.EventManager()
    ghost_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    pacman_position = (1 * CELL_SIZE, 1 * CELL_SIZE)
    pacman = Pacman.Pacman(eventManager,pacman_position[0], pacman_position[1], "images/Pacman.png")
    all_sprites.add(pacman)

   # Add some ghosts
    blueGhost = Ghost.Ghost(eventManager, 14 * CELL_SIZE, 18 * CELL_SIZE, "images/BlueGhost.png", Ghost.SearchAlgorigthmName.BFS, pacman_position)
    orangeGhost = Ghost.Ghost(eventManager, 9 * CELL_SIZE, 25* CELL_SIZE, "images/OrangeGhost.png", Ghost.SearchAlgorigthmName.UCS, pacman_position)
    redGhost = Ghost.Ghost(eventManager, 15 * CELL_SIZE, 15 * CELL_SIZE, "images/RedGhost.png", Ghost.SearchAlgorigthmName.A_STAR, pacman_position)
    pinkGhost = Ghost.Ghost(eventManager, 14 * CELL_SIZE , 15 * CELL_SIZE, "images/PinkGhost.png", Ghost.SearchAlgorigthmName.DFS, pacman_position)
    ghost_group.add(blueGhost)
    ghost_group.add(orangeGhost)
    ghost_group.add(redGhost)
    ghost_group.add(pinkGhost)
    all_sprites.add(blueGhost)
    all_sprites.add(orangeGhost)
    all_sprites.add(redGhost)
    all_sprites.add(pinkGhost)


    running = True
    clock = pygame.time.Clock()

    # Publish the event to ghost to start moving
    eventManager.publish("PACMAN_MOVED", None)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        orangeGhost.AutoMove()
        pinkGhost.AutoMove()
        blueGhost.AutoMove()
        redGhost.AutoMove()

        pygame.time.delay(400)
        # Check collision between pacman and ghosts
        hits = pygame.sprite.spritecollide(pacman, ghost_group, False)
        if hits:
            running = False
            # Display a game over message and stop the game
            font = pygame.font.Font(None, 36)
            text = font.render(f"Game Over", True, RED)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(1000)
            break
        
        
        # Rerender the screen
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()