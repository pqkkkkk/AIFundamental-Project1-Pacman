import pygame
from objects import Coin
from objects import Ghost
from objects import Pacman
from objects import EventManager
from objects import ScoreManager
from images import *
import time, imageio
import os
from Global import WIDTH, HEIGHT, CELL_SIZE, RED, WHITE, CreateBackground, game_map, PACMAN_POSITION
import SearchAlgorithms
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
    # initial variables to caculate time and memory usage here
    start_time = time.time()
    if not os.path.exists("frames"):
        os.makedirs("frames")
    frames = []  # Lưu tên file ảnh tạm
    frame_index = 0

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
            screen.fill("black")
            
            # font 
            GameOver_font = pygame.font.Font(None, 60)
            info_font = pygame.font.Font(None, 30)

            # Text
            GameOver_text = GameOver_font.render(f"Game over", True, RED)
            time_text = info_font.render(f"Time: {SearchAlgorithms.timeSpend:.4f}s", True, WHITE)
            mem_text = info_font.render(f"Memory: {SearchAlgorithms.memoryUsage:.3f} MB", True, WHITE)
            # Number of node expanded is the number of node that pacman came in the path to reach goal
            nodeExpanded_text = info_font.render(f"{SearchAlgorithms.expandedNode} nodes expanded", True, WHITE)
            
            # Nút Exit
            button_font = pygame.font.Font(None, 30)
            button_text = button_font.render("Exit", True, (255, 255, 255))
            button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 100, 120, 40)  # x, y, width, height
            button_text_rect = button_text.get_rect(center=button_rect.center)

            # Vẽ lên màn hình 
            screen.blit(GameOver_text, (WIDTH // 2 - 100, HEIGHT // 2 - 130 ))
            screen.blit(nodeExpanded_text, (WIDTH // 2 - 90, HEIGHT // 2 - 50))
            screen.blit(time_text, (WIDTH // 2 - 60, HEIGHT // 2))
            screen.blit(mem_text, (WIDTH // 2 - 90, HEIGHT // 2 + 50))
            pygame.draw.rect(screen, RED, button_rect)  # Nền nút
            screen.blit(button_text, button_text_rect)
            
            pygame.display.flip()
            frame_path = f"frames/frame_{frame_index:04d}.png"
            pygame.image.save(screen, frame_path)
            frames.append(frame_path)
            frame_index += 1
            
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
        frame_path = f"frames/frame_{frame_index:04d}.png"
        pygame.image.save(screen, frame_path)
        frames.append(frame_path)
        frame_index += 1

        clock.tick(60)
    
    pygame.quit()
    
    def export_gif_from_frames(frames, output_path="pacman_gameplay.gif", fps=5):
        images = []
        for frame_path in frames:
            images.append(imageio.imread(frame_path))
        imageio.mimsave(output_path, images, fps=fps)
        print(f"GIF saved to {output_path}")

    export_gif_from_frames(frames, f"pacman_level{level}_gameplay.gif", fps=5)

    # Xoá file frame tạm
    for f in frames:
        if os.path.exists(f):
            os.remove(f)