import pygame
from objects import Coin
from objects import Ghost
from objects import Pacman
from objects import EventManager
from objects import ScoreManager
from images import *
import os
from Global import WIDTH, HEIGHT, CELL_SIZE, RED, CreateBackground, game_map

def RunGameOfLevel6():
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    os.chdir(source_dir)
    
    pygame.init()
    
    # Screen settings
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")

    # Creating a map
    map_width = WIDTH // CELL_SIZE
    map_height = HEIGHT // CELL_SIZE
    map = game_map
    
    # Background
    background = CreateBackground()
    # Create objects
    eventManager = EventManager.EventManager()
    scoreManager = ScoreManager.ScoreManager(eventManager)
    coin_group = pygame.sprite.Group()
    ghost_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    pacman = Pacman.Pacman(eventManager,3 * CELL_SIZE, 5 * CELL_SIZE, "images/Pacman.png")
    all_sprites.add(pacman)

    
    # Adding some coins for demonstration
    map[2][2] = 2
    map[3][3] = 2
    # Add coins
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 2:
                coin = Coin.Coin(x * CELL_SIZE, y * CELL_SIZE)
                coin_group.add(coin)
                all_sprites.add(coin)
    # Add some ghosts
    blueGhost = Ghost.Ghost(eventManager, 10 * CELL_SIZE, 10 * CELL_SIZE, "images/BlueGhost.png", Ghost.SearchAlgorigthmName.BFS, (1 * CELL_SIZE, 1 * CELL_SIZE))
    orangeGhost = Ghost.Ghost(eventManager, 11 * CELL_SIZE, 11* CELL_SIZE, "images/OrangeGhost.png", Ghost.SearchAlgorigthmName.UCS, (1 * CELL_SIZE, 1 * CELL_SIZE))
    redGhost = Ghost.Ghost(eventManager, 12* CELL_SIZE, 12 * CELL_SIZE, "images/RedGhost.png", Ghost.SearchAlgorigthmName.A_STAR, (1 * CELL_SIZE, 1 * CELL_SIZE))
    pinkGhost = Ghost.Ghost(eventManager, 14 * CELL_SIZE , 14 * CELL_SIZE, "images/PinkGhost.png", Ghost.SearchAlgorigthmName.DFS, (1 * CELL_SIZE, 1 * CELL_SIZE))
    ghost_group.add(blueGhost)
    ghost_group.add(orangeGhost)
    ghost_group.add(redGhost)
    ghost_group.add(pinkGhost)
    all_sprites.add(blueGhost)
    all_sprites.add(orangeGhost)
    all_sprites.add(redGhost)
    all_sprites.add(pinkGhost)

    # Điểm số
    score = 0
    font = pygame.font.SysFont(None, 24)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not pacman.CheckCollisionWithWallIfMove(event,map):
                    pacman.OnKeyDown(event)
                    pacman.Update()
        
        # Check collision between pacman and ghosts
        hits = pygame.sprite.spritecollide(pacman, ghost_group, False)
        if hits:
            running = False
            # Display a game over message and stop the game
            font = pygame.font.Font(None, 36)
            text = font.render(f"Game Over. Score : {score}", True, RED)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            break
        
        # Check collision between pacman and coins
        hits = pygame.sprite.spritecollide(pacman, coin_group, True) # True to remove the coin
        for coin in hits:
            score += 10
        
        # Rerender the screen
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

         # Draw the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (0, 0))

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()