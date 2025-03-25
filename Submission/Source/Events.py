from enum import Enum

class Events(Enum):
    PACMAN_MOVE = "PACMAN_MOVE",
    PACMAN_CAUGHT = "PACMAN_CAUGHT",
    COIN_EATEN = "COIN_EATEN",