import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 32
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman với Sprite và Group")

# Định nghĩa class Pacman
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (16, 16), 16)  # Pacman màu vàng
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        if direction == 'left': self.rect.x -= 4
        if direction == 'right': self.rect.x += 4
        if direction == 'up': self.rect.y -= 4
        if direction == 'down': self.rect.y += 4

# Định nghĩa class Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 165, 0), (8, 8), 8)  # Coin màu cam
        self.rect = self.image.get_rect(topleft=(x, y))

# Tạo các group
all_sprites = pygame.sprite.Group()  # Group chứa tất cả sprite
coin_group = pygame.sprite.Group()  # Group chứa các coin

# Tạo Pacman
pacman = Pacman(32, 32)
all_sprites.add(pacman)

# Tạo các coin
for y in range(5):
    for x in range(5):
        if (x, y) in [(1, 2), (3, 2), (2, 3)]:  # Vị trí coin
            coin = Coin(x * CELL_SIZE, y * CELL_SIZE)
            coin_group.add(coin)
            all_sprites.add(coin)

# Vẽ background (giả lập)
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 0, 0))
pygame.draw.rect(background, (0, 0, 255), (100, 100, 600, 400), 5)

# Điểm số
score = 0
font = pygame.font.SysFont(None, 36)

# Vòng lặp chính
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật vị trí Pacman
    direction = None
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: direction = 'left'
    if keys[pygame.K_RIGHT]: direction = 'right'
    if keys[pygame.K_UP]: direction = 'up'
    if keys[pygame.K_DOWN]: direction = 'down'
    pacman.update(direction)

    # Kiểm tra va chạm với coin
    hits = pygame.sprite.spritecollide(pacman, coin_group, True)  # True: Xóa coin khi va chạm
    for coin in hits:
        score += 10

    # Vẽ lại màn hình
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Vẽ điểm số
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()