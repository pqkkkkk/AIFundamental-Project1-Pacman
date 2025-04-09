import pygame
from game_options.Level6 import RunGameOfLevel6
from game_options.Level1To4 import RunGameOfAnyLevelFrom1To4
from game_options.Level5 import RunGameOfLevel5

def RunGameOfLevel(level):
    print(f"Running Level {level}")
    if level == 1:
        RunGameOfAnyLevelFrom1To4(level)
    elif level == 2:
        RunGameOfAnyLevelFrom1To4(level)
    elif level == 3:
        RunGameOfAnyLevelFrom1To4(level)
    elif level == 4:
        RunGameOfAnyLevelFrom1To4(level)
    elif level == 5:
        RunGameOfLevel5()
    elif level == 6:
        RunGameOfLevel6()
    else:
        print("Invalid level selected")
    
def ShowLevelSelection():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Select Level")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    levels = [1, 2, 3, 4, 5, 6]
    selected_level = None

    while selected_level is None:
        screen.fill((0, 0, 0))
        y_offset = 100
        for level in levels:
            text = font.render(f"Level {level}", True, (255, 255, 255))
            text_rect = text.get_rect(center=(300, y_offset))
            screen.blit(text, text_rect)
            y_offset += 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_level = 1
                elif event.key == pygame.K_2:
                    selected_level = 2
                elif event.key == pygame.K_3:
                    selected_level = 3
                elif event.key == pygame.K_4:
                    selected_level = 4
                elif event.key == pygame.K_5:
                    selected_level = 5
                elif event.key == pygame.K_6:
                    selected_level = 6

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return selected_level

if __name__ == "__main__":
    selected_level = ShowLevelSelection()
    RunGameOfLevel(selected_level)
