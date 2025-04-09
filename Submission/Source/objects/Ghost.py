import pygame
from enum import Enum
from SearchAlgorithms import *

from Global import WIDTH, HEIGHT, CELL_SIZE, RED, CreateBackground, game_map, PACMAN_POSITION

class SearchAlgorigthmName(Enum):
    A_STAR = "A_STAR"
    BFS = "BFS"
    DFS = "DFS"
    UCS = "UCS"

class Ghost(pygame.sprite.Sprite):
    @staticmethod
    def executeSearchPacman(searchAlgorigthmName, map, start, goal):
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
        self.currentPositionInPath = 0
        self.searchAlgorigthmName = searchAlgorigthmName
        self.avatar = pygame.image.load(image)
        self.eventManager = eventManager
        eventManager.subscribe("PACMAN_MOVED",self.OnPacmanMoved)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.image.blit(self.avatar, (0, 0))
        self.rect = self.image.get_rect(top=x, left=y)
    
    def OnPacmanMoved(self, data):
        self.path = Ghost.executeSearchPacman(self.searchAlgorigthmName, game_map, (self.x // CELL_SIZE, self.y // CELL_SIZE), (self.pacman_position[0] // CELL_SIZE, self.pacman_position[1] // CELL_SIZE))
        self.currentPositionInPath = 0
    
    def AutoMove(self):
        if self.currentPositionInPath < len(self.path):
            self.x= self.path[self.currentPositionInPath][0] * CELL_SIZE
            self.y = self.path[self.currentPositionInPath][1] * CELL_SIZE
            self.rect = pygame.Rect(self.y, self.x, CELL_SIZE, CELL_SIZE)
            self.currentPositionInPath += 1
        else:
            pass
        