<<<<<<< Updated upstream
import pygame as pg
import numpy as np
=======
from enum import Enum
from random import choice
>>>>>>> Stashed changes

import numpy as np
import pygame as pg

ORANGE_RICKY = [
<<<<<<< Updated upstream
    [False, False, True],
    [True, True, True]
]
BLUE_RICKY = [
    [True, False, False],
    [True, True, True]
]
CLEVELAND_Z = [
    [True, True, False],
    [False, True, True]
]
RHODE_ISLAND_Z = [
    [False, True, True],
    [True, True, False]
=======
    [None, None, True],
    [True, True, True]
]
BLUE_RICKY = [
    [True, None, False],
    [True, True, True]
]
CLEVELAND_Z = [
    [True, True, None],
    [None, True, True]
]
RHODE_ISLAND_Z = [
    [None, True, True],
    [True, True, None]
>>>>>>> Stashed changes
]
HERO = [
    [True, True, True, True]
]
TEEWEE = [
<<<<<<< Updated upstream
    [False, True, False],
=======
    [None, True, None],
>>>>>>> Stashed changes
    [True, True, True]
]
SMASHBOY = [
    [True, True],
    [True, True]
<<<<<<< Updated upstream
=======
]
SHAPES = list(map(np.array, [
    BLUE_RICKY,
    CLEVELAND_Z,
    HERO,
    ORANGE_RICKY,
    RHODE_ISLAND_Z,
    SMASHBOY,
    TEEWEE,
]))

COLORS = [
    "orange",
    "blue",
    "red",
    "green",
    "cyan",
    "purple",
    "yellow",
>>>>>>> Stashed changes
]
BLOCKS = list(map(np.array, [
    BLUE_RICKY,
    CLEVELAND_Z,
    HERO,
    ORANGE_RICKY,
    RHODE_ISLAND_Z,
    SMASHBOY,
    TEEWEE,
]))


class Block:
    def __init__(self, shape: list[np.ndarray], size: tuple[int, int] = (20, 20)):
        self.shape: list[np.ndarray] = shape
        self.size: tuple[int, int] = size

    def draw(self, display):
        # Iterate over shape and draw rectangles
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column]:
                    rect = pg.Rect((20 + 20 * column, 20 + 20 * row), (20, 20))
                    pg.draw.rect(display, "orange", rect)

<<<<<<< Updated upstream
=======
class Block:
    def __init__(self, shape: list[np.ndarray], grid: list[list], screen_size: tuple[int, int]):
        self.grid: list[list] = grid
        self.shape: list[np.ndarray] = shape
        self.block_size: tuple[int, int] = (20, 20)
        self.step: int = 20
        self.screen_size: tuple[int, int] = screen_size

        self.start_x: int = int(self.screen_size[0] / (self.step * 2))
        self.start_y: int = 0
        self.end_x: int = self.start_x + len(self.shape[0]) - 1
        self.end_y: int = self.start_y + len(self.shape) - 1

        self.shift: int = 0
        print(self.shape, self.end_y, self.start_y - 1, self.end_x, self.start_x - 1)

    def add_to_grid(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                self.grid[i][j + self.start_x] = self.shape[i][j]

    def fall(self, level):
        for row in range(self.end_y, self.start_y - 1, -1):
            for block in range(self.end_x, self.start_x - 1, -1):
                self.grid[row + 1 + level][block] = self.grid[row + level][block]
                self.grid[row + level][block] = None

    def __move(self, direction: Direction):
        match direction:
            case Direction.RIGHT:
                self.shift += 1
            case Direction.LEFT:
                self.shift -= 1

>>>>>>> Stashed changes
    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.shape = np.rot90(self.shape, 1)
<<<<<<< Updated upstream
                
=======
            if event.key == pg.K_RIGHT:
                self.__move(Direction.RIGHT)
            if event.key == pg.K_LEFT:
                self.__move(Direction.LEFT)
>>>>>>> Stashed changes
