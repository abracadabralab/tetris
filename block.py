from random import choice

import numpy as np
import pygame as pg
from enum import Enum

ORANGE_RICKY = [
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
]
HERO = [
    [True, True, True, True]
]
TEEWEE = [
    [False, True, False],
    [True, True, True]
]
SMASHBOY = [
    [True, True],
    [True, True]
]
SHAPES = list(map(np.array, [
    ORANGE_RICKY,
    BLUE_RICKY,
    CLEVELAND_Z,
    RHODE_ISLAND_Z,
    HERO,
    TEEWEE,
    SMASHBOY,
]))

COLORS = {
    1: "orange",
    2: "blue",
    3: "red",
    4: "green",
    5: "cyan",
    6: "purple",
    7: "yellow",
}


class Direction(Enum):
    RIGHT = 1
    LEFT = 2


class Block:
    def __init__(self, random_num: int, grid: list[list], screen_size: tuple[int, int]):
        self.screen_size: tuple[int, int] = screen_size
        self.grid: list[list] = grid
        self.random_number: int = random_num

        self.shape: np.ndarray = SHAPES[random_num]
        self.block_size: tuple[int, int] = (20, 20)
        self.step: int = 20
        self.color: str = COLORS[random_num + 1]
        self.level: int = 0

        self.start_x: int = int(self.screen_size[0] / (self.step * 2))
        self.start_y: int = 0
        self.end_x: int = self.start_x + len(self.shape[0]) - 1
        self.end_y: int = self.start_y + len(self.shape) - 1

        self.shift: int = 0

    def add_to_grid(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                self.grid[i][j + self.start_x] = self.color if self.shape[i][j] else 0

    def fall(self):
        for row in range(self.end_y, self.start_y - 1, -1):
            for block in range(self.end_x, self.start_x - 1, -1):
                if self.grid[row + 1][block] == 0:
                    self.grid[row + 1][block] = self.color \
                        if self.grid[row][block] else 0
                self.grid[row][block] = 0
        self.start_y += 1
        self.end_y += 1

    def __move(self, direction: Direction):
        match direction:
            case Direction.RIGHT:
                self.shift = 1
            case Direction.LEFT:
                self.shift = -1
        for row in range(self.end_y + 1, self.start_y - 1, -1):
            for block in range(self.end_x, self.start_x - 1, -1):
                if self.grid[row][block] != 0:
                    self.grid[row][block + self.shift] = self.grid[row][block]
                    self.grid[row][block] = 0
        match direction:
            case Direction.RIGHT:
                self.start_x += 1
                self.end_x += 1
            case Direction.LEFT:
                self.start_x -= 1
                self.end_x -= 1

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.shape = np.rot90(self.shape, 1)
            if event.key == pg.K_RIGHT:
                self.__move(Direction.RIGHT)
            if event.key == pg.K_LEFT:
                self.__move(Direction.LEFT)
            if event.key == pg.K_0:
                self.__move(Direction.RIGHT)

    def can_fall(self) -> bool:
        n = [*range(self.start_x + self.shift, self.end_x + self.shift + 1)]
        if self.level > self.screen_size[1] / self.step - len(self.shape) - 1:
            return False

        for i in range(len(self.shape[0])):
            if self.shape[-1][i]:
                if self.grid[self.level + len(self.shape)][n[i]]:
                    return False
        return True
