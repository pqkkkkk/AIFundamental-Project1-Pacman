import pygame
from objects import Coin
from objects import Ghost
from objects import Pacman
from objects import EventManager
from objects import ScoreManager
from images import *
import os
from Global import WIDTH, HEIGHT, CELL_SIZE, RED, BLACK, CreateBackground, game_map

def RunGameOfLevel6():
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    os.chdir(source_dir)
    
    pygame.init()
    
    pygame.mixer.init()
    pygame.mixer.music.load("images/pacman_beginning.wav")
    pygame.mixer.music.play(-1)  # Play the music in a loop
    pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)

    # Screen settings
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")

    # Creating a map
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

    # Add coins
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                coin = Coin.Coin(x * CELL_SIZE, y * CELL_SIZE)
                coin_group.add(coin)
                all_sprites.add(coin)
    # Add some ghosts
    blueGhost = Ghost.Ghost(eventManager, 10 * CELL_SIZE, 10 * CELL_SIZE, "images/BlueGhost.png", Ghost.SearchAlgorigthmName.BFS, (3 * CELL_SIZE, 5 * CELL_SIZE))
    orangeGhost = Ghost.Ghost(eventManager, 11 * CELL_SIZE, 11* CELL_SIZE, "images/OrangeGhost.png", Ghost.SearchAlgorigthmName.UCS, (3 * CELL_SIZE, 5 * CELL_SIZE))
    redGhost = Ghost.Ghost(eventManager, 12* CELL_SIZE, 12 * CELL_SIZE, "images/RedGhost.png", Ghost.SearchAlgorigthmName.A_STAR, (3 * CELL_SIZE, 5 * CELL_SIZE))
    pinkGhost = Ghost.Ghost(eventManager, 14 * CELL_SIZE , 14 * CELL_SIZE, "images/PinkGhost.png", Ghost.SearchAlgorigthmName.DFS, (3 * CELL_SIZE, 5 * CELL_SIZE))
    ghost_group.add(blueGhost)
    ghost_group.add(orangeGhost)
    ghost_group.add(redGhost)
    ghost_group.add(pinkGhost)
    all_sprites.add(blueGhost)
    all_sprites.add(orangeGhost)
    all_sprites.add(redGhost)
    all_sprites.add(pinkGhost)

    # Game score
    score = 0
    font = pygame.font.SysFont(None, 24)
    
    # Variable to control ghost movement
    frameCouter = 0
    ghostMoveInterval = 10

    running = True
    clock = pygame.time.Clock()

    # Publish the event to ghost to start moving
    eventManager.publish("PACMAN_MOVED", None)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not pacman.CheckCollisionWithWallIfMove(event,map):
                    pacman.OnKeyDown(event)
                    pacman.Update(frameCouter)
        
        frameCouter += 1

        if frameCouter >= 70:
            ghostMoveInterval = 14
        if frameCouter >= 100:
            ghostMoveInterval = 13
        if frameCouter>= 160:
            ghostMoveInterval = 12

        if frameCouter % ghostMoveInterval == 0:
            orangeGhost.AutoMove()
            pinkGhost.AutoMove()
            blueGhost.AutoMove()
            redGhost.AutoMove()
        
        # Check collision between pacman and coins
        hits = pygame.sprite.spritecollide(pacman, coin_group, True) # True to remove the coin
        for coin in hits:
            score += 1
        
        # Check collision between pacman and ghosts. If true, game over
        ghost_hits = pygame.sprite.spritecollide(pacman, ghost_group, False)
        if ghost_hits:
            running = False
            # Display a game over message and stop the game
            killer_ghost = ghost_hits[0]

            # Gán tên dựa theo thuật toán tìm đường
            ghost_name = "Unknown"
            if killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.BFS:
                ghost_name = "Blue Ghost (BFS)"
            elif killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.DFS:
                ghost_name = "Pink Ghost (DFS)"
            elif killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.UCS:
                ghost_name = "Orange Ghost (UCS)"
            elif killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.A_STAR:
                ghost_name = "Red Ghost (A*)"
    
            screen.fill("black")
            font = pygame.font.Font(None, 60)
            info_font = pygame.font.Font(None, 32)

            text = font.render(f"Game Over", True, RED)
            result = info_font.render(f"Score: {score} coins", True, (255, 255, 255))
            killer = info_font.render(f"Killer: {ghost_name}", True, (255,255,255))

            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
            result_rect = result.get_rect(center=(WIDTH//2, HEIGHT//2 + 30))
            killer_rect = killer.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
                            
            # Nút exit
            button_font = pygame.font.Font(None, 30)
            button_text = button_font.render("Exit", True, (255, 255, 255))
            button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 70, 120, 40)  # x, y, width, height
            button_text_rect = button_text.get_rect(center=button_rect.center)

            # vẽ lên màn hình
            screen.blit(text, text_rect)
            screen.blit(killer, killer_rect)
            screen.blit(result, result_rect)
            pygame.draw.rect(screen, RED, button_rect)  # Nền nút
            screen.blit(button_text, button_text_rect)

            pygame.display.flip()
            
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_rect.collidepoint(event.pos):
                            waiting = False
            break

        
        # Rerender the screen
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

         # Draw the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (0, 0))

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()