import pygame

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước màn hình
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Map")

# Màu sắc
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Kích thước ô
TILE_SIZE = 40

# Bản đồ (1 = tường, 0 = đường đi, 2 = chấm nhỏ)
map_layout = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,2,1],
    [1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,2,1],
    [1,2,2,2,2,1,2,2,2,1,1,2,2,2,1,2,2,2,2,1],
    [1,1,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1],
    [1,1,1,1,2,1,2,2,2,2,2,2,2,2,1,2,1,1,1,1],
    [1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,2,1],
    [1,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Vị trí ban đầu của Pac-Man
pacman_pos = [TILE_SIZE, TILE_SIZE]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Vẽ bản đồ
    screen.fill(BLACK)
    
    for row in range(len(map_layout)):
        for col in range(len(map_layout[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            
            # Vẽ tường
            if map_layout[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
            
            # Vẽ chấm nhỏ
            elif map_layout[row][col] == 2:
                pygame.draw.circle(screen, WHITE, 
                                 (x + TILE_SIZE//2, y + TILE_SIZE//2), 
                                 5)
    
    # Vẽ Pac-Man
    pygame.draw.circle(screen, YELLOW, 
                      (int(pacman_pos[0] + TILE_SIZE//2), 
                       int(pacman_pos[1] + TILE_SIZE//2)), 
                      TILE_SIZE//2 - 2)
    
    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)

pygame.quit()