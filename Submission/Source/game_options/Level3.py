import os
import pygame
import sys

from objects import Pacman
from objects import Coin
from objects import Ghost
from objects import EventManager
from objects import ScoreManager 
from SearchAlgorithms import UCS_Algorithm

currentFilePath = os.path.abspath(__file__)
dirPath = os.path.dirname(currentFilePath)
source_dir = os.path.join(dirPath, '..')
os.chdir(source_dir)
def RunGameOfLevel3():
    # Khởi tạo ban đầu và thiết lập
    pygame.init()
    width = 900
    height = 600
    CELL_SIZE = 30
    screen = pygame.display.set_mode((width, height))
    timer = pygame.time.Clock()
    fps = 60
    
    # vẽ bản đồ (test - bỏ khi có bảng đồ mới)
    game_map = [
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    screen.fill('black')
    # Tìm đường đi và tính toán chi phí
    cost, path = UCS_Algorithm(game_map, (0,0), (11,10))
    
    # Vẽ map (test - sửa khi có map mới)
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if(game_map[i][j] == 1):
                pygame.draw.rect(screen, (0,0, 255), (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # khởi tạo bộ quản lý event và ghosts và pacman
    eventManager = EventManager.EventManager()
    orangeGhost = Ghost.Ghost(eventManager, 0 , 0, "images/OrangeGhost.png")
    pacman = Pacman.Pacman(eventManager, 10 * CELL_SIZE, 11 * CELL_SIZE,  "images/Pacman.png")
    # Khởi tạo vị trí ban đầu
    pacman.Draw(screen)
    orangeGhost.Draw(screen)         
    currentIndex = 0
    length = len(path)
    running = True
    # lấy thời gian khi chương trình bắt đầu chạy
    start_time = pygame.time.get_ticks()
    
    while running:
        
        timer.tick(fps)       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Kiểm tra đến vị trí cuối, thì dừng 
        if currentIndex < length-1:
            pygame.time.delay(300)
            currentIndex += 1

        # Xoá ma ở vị trí cũ
        pygame.draw.rect(screen, (0, 0, 0), (orangeGhost.x, orangeGhost.y, CELL_SIZE, CELL_SIZE))         

        # Nếu ma đã bắt được pacman, hiện thời gian thực thi, chi phí và nút exit
        if pacman.x == orangeGhost.x and pacman.y == orangeGhost.y:
            # Lấy thời gian sau khi pacman đã bị bắt
            end_time = pygame.time.get_ticks()
            elapsed_time = (end_time - start_time) / 1000  # tính thời gian và đổi sang giây (end_time và start_time ở dạng miligiay)
            font = pygame.font.Font(None, 50)
            
            info_text = f'Time: {elapsed_time:.2f}s | Cost: {cost}'
            text_surface = font.render(info_text, True, (255, 255, 255))
            
            exit_rect = pygame.Rect(width // 2 - 50, height // 2 + 30, 100, 50) # nút exit
            
            # Code click exit để kết thúc
            while True:
                screen.fill((0, 0, 0))
                screen.blit(text_surface, (width // 2 - 150, height // 2 - 50))
                pygame.draw.rect(screen, (255, 0, 0), exit_rect)
                exit_text = font.render("Exit", True, (255, 255, 255))
                screen.blit(exit_text, (width // 2 - 25, height // 2 + 40))
                pygame.display.flip()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()        
           
        # Vẽ ma ở vị trí mới
        orangeGhost.x = path[currentIndex][1]*CELL_SIZE
        orangeGhost.y = path[currentIndex][0]*CELL_SIZE
        orangeGhost.Draw(screen)
        
        pygame.display.flip()
        

    pygame.quit()
