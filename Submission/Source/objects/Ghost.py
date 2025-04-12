import pygame
from enum import Enum
from SearchAlgorithms import *

from Global import CELL_SIZE, game_map, PACMAN_POSITION

class SearchAlgorigthmName(Enum):
    A_STAR = "A_STAR"
    BFS = "BFS"
    DFS = "DFS"
    UCS = "UCS"

class Ghost(pygame.sprite.Sprite):
    @staticmethod
    def ExecuteSearchPacman(searchAlgorigthmName, map, start, goal):
        path = []
        if searchAlgorigthmName == SearchAlgorigthmName.A_STAR:
            path = a_star_search(map, start, goal)
        elif searchAlgorigthmName == SearchAlgorigthmName.BFS:
            path = bfs_search(map, start, goal)
        elif searchAlgorigthmName == SearchAlgorigthmName.DFS:
            path = dfs_search(map, start, goal)
        elif searchAlgorigthmName == SearchAlgorigthmName.UCS:
            path = ucs_search(map, start, goal)

        return path if path is not None else []

    def __init__(self,eventManager,x,y,image, searchAlgorigthmName, pacman_position):
        super().__init__()
        self.x = x
        self.y = y
        self.pacman_position = pacman_position
        self.path = []
        self.updatePathInterval = 15
        self.currentPositionInPath = 0
        self.searchAlgorigthmName = searchAlgorigthmName
        self.avatar = pygame.image.load(image)
        self.eventManager = eventManager
        eventManager.subscribe("PACMAN_MOVED",self.OnPacmanMoved)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.image.blit(self.avatar, (0, 0))
        self.rect = self.image.get_rect(top=x, left=y)
    
    def OnPacmanMoved(self, data):
        if data is None:
            self.path = Ghost.ExecuteSearchPacman(self.searchAlgorigthmName, game_map, (self.x // CELL_SIZE, self.y // CELL_SIZE), (self.pacman_position[0] // CELL_SIZE, self.pacman_position[1] // CELL_SIZE))
            self.currentPositionInPath = 0
        elif data["frameCounter"] % 15 == 0:
            self.pacman_position = (data["x"], data["y"])
            self.path = Ghost.ExecuteSearchPacman(self.searchAlgorigthmName, game_map, (self.x // CELL_SIZE, self.y // CELL_SIZE), (self.pacman_position[0] // CELL_SIZE, self.pacman_position[1] // CELL_SIZE))
            self.currentPositionInPath = 0
        elif self.currentPositionInPath >= len(self.path):
            self.pacman_position = (data["x"], data["y"])
            self.path = Ghost.ExecuteSearchPacman(self.searchAlgorigthmName, game_map, (self.x // CELL_SIZE, self.y // CELL_SIZE), (self.pacman_position[0] // CELL_SIZE, self.pacman_position[1] // CELL_SIZE))
            self.currentPositionInPath = 0
        
    @staticmethod
    def CheckCollisionIfMoveWithAnotherGhost(new_x, new_y):
        if game_map[int(new_x / CELL_SIZE)][int(new_y / CELL_SIZE)] == -1:
            print("Collision with another ghost")
            return True
        return False
    
    def AutoMove(self):
        if self.currentPositionInPath >= len(self.path):
            return

        new_x = self.path[self.currentPositionInPath][0] * CELL_SIZE
        new_y = self.path[self.currentPositionInPath][1] * CELL_SIZE

        if self.CheckCollisionIfMoveWithAnotherGhost(new_x, new_y):
            self.path = Ghost.ExecuteSearchPacman(self.searchAlgorigthmName, game_map, (self.x // CELL_SIZE, self.y // CELL_SIZE), (self.pacman_position[0] // CELL_SIZE, self.pacman_position[1] // CELL_SIZE))
            self.currentPositionInPath = 0
        
        game_map[int(self.x / CELL_SIZE)][int(self.y / CELL_SIZE)] = 0
        self.x= new_x
        self.y = new_y
        game_map[int(self.x / CELL_SIZE)][int(self.y / CELL_SIZE)] = -1
        self.rect = pygame.Rect(self.y, self.x, CELL_SIZE, CELL_SIZE)
        self.currentPositionInPath += 1
        