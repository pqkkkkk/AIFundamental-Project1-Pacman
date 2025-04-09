import pygame
from objects import Coin
from objects import Ghost
from objects import Pacman
from objects import EventManager
from objects import ScoreManager
from images import *
import os
from Global import WIDTH, HEIGHT, CELL_SIZE, RED, CreateBackground, game_map, PACMAN_POSITION

def RunGameOfAnyLevelFrom1To4(level):
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    os.chdir(source_dir)
    
    pygame.init()
    
    # Screen settings
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")

    # Creating a map
    map = game_map
    
    # Background
    background = CreateBackground()
    # Create objects
    eventManager = EventManager.EventManager()
    ghost_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    pacman = Pacman.Pacman(eventManager,1 * CELL_SIZE, 1 * CELL_SIZE, "images/Pacman.png")
    all_sprites.add(pacman)
    global PACMAN_POSITION
    PACMAN_POSITION = (2 * CELL_SIZE, 2 * CELL_SIZE)

    # Add some ghosts
    searchAlgorithmName = Ghost.SearchAlgorigthmName.UCS
    ghostAvatar = "images/BlueGhost.png"
    if level == 1:
        searchAlgorithmName = Ghost.SearchAlgorigthmName.BFS
        ghostAvatar = "images/BlueGhost.png"
    elif level == 2:
        searchAlgorithmName = Ghost.SearchAlgorigthmName.DFS
        ghostAvatar = "images/PinkGhost.png"
    elif level == 3:
        searchAlgorithmName = Ghost.SearchAlgorigthmName.UCS
        ghostAvatar = "images/OrangeGhost.png"
    elif level == 4:
        searchAlgorithmName = Ghost.SearchAlgorigthmName.A_STAR
        ghostAvatar = "images/RedGhost.png"

    ghost = Ghost.Ghost(eventManager, 10 * CELL_SIZE, 10 * CELL_SIZE,
                               ghostAvatar, searchAlgorithmName,
                               (1 * CELL_SIZE,1 * CELL_SIZE))
    ghost_group.add(ghost)
    all_sprites.add(ghost)


    running = True
    clock = pygame.time.Clock()

    # Publish the event to ghost to start moving
    eventManager.publish("PACMAN_MOVED", None)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ghost.AutoMove()

        pygame.time.delay(200)
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