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
    coin_group = pygame.sprite.Group()

    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if game_map[y][x] == 0:
                coin = Coin.Coin(x * CELL_SIZE, y * CELL_SIZE)
                coin_group.add(coin)
                all_sprites.add(coin)

    pacman_position = (7 * CELL_SIZE, 1 * CELL_SIZE)
    pacman = Pacman.Pacman(eventManager,pacman_position[0], pacman_position[1], "images/Pacman.png")
    all_sprites.add(pacman)

   # Add some ghosts
    blueGhost = Ghost.Ghost(eventManager, 10 * CELL_SIZE, 10 * CELL_SIZE, "images/BlueGhost.png", Ghost.SearchAlgorigthmName.BFS, pacman_position)
    orangeGhost = Ghost.Ghost(eventManager, 11 * CELL_SIZE, 11* CELL_SIZE, "images/OrangeGhost.png", Ghost.SearchAlgorigthmName.UCS, pacman_position)
    redGhost = Ghost.Ghost(eventManager, 12* CELL_SIZE, 12 * CELL_SIZE, "images/RedGhost.png", Ghost.SearchAlgorigthmName.A_STAR, pacman_position)
    pinkGhost = Ghost.Ghost(eventManager, 14 * CELL_SIZE , 14 * CELL_SIZE, "images/PinkGhost.png", Ghost.SearchAlgorigthmName.DFS, pacman_position)
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

    # Tính thời gian tìm được pacman
    start_ticks = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        orangeGhost.AutoMove()
        pinkGhost.AutoMove()
        blueGhost.AutoMove()
        redGhost.AutoMove()

        pygame.time.delay(300)
        # Check collision between pacman and ghosts
        hits = pygame.sprite.spritecollide(pacman, ghost_group, False)
        if hits:
            running = False
            elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000  # tính bằng giây
            killer_ghost = hits[0]  # ghost đầu tiên va chạm

            # Gán tên dựa theo thuật toán tìm đường
            ghost_name = "Unknown"
            if killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.BFS:
                ghost_name = "BlueGhost (BFS)"
            elif killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.DFS:
                ghost_name = "PinkGhost (DFS)"
            elif killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.UCS:
                ghost_name = "OrangeGhost (UCS)"
            elif killer_ghost.searchAlgorigthmName == Ghost.SearchAlgorigthmName.A_STAR:
                ghost_name = "RedGhost (A*)"
    
            # Display a game over message and stop the game
            screen.fill("black")
            
            font = pygame.font.Font(None, 48)
            info_font = pygame.font.Font(None, 30)
            # Game over
            text = font.render(f"Game Over", True, RED)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60))
            
            # time run
            time_text = info_font.render(f"Time: {elapsed_time} seconds", True, (255, 255, 255))
            time_rect = time_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
            
            # pacman killer
            killer_text = info_font.render(f"Killer: {ghost_name}", True, (255, 255, 255))
            killer_rect = killer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

            # nút exit
            button_text = info_font.render("Exit", True, (255, 255, 255))
            button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 60, 120, 40)  # x, y, width, height
            button_text_rect = button_text.get_rect(center=button_rect.center)
            
            screen.blit(text, text_rect)
            screen.blit(time_text, time_rect)
            screen.blit(killer_text, killer_rect)
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

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()