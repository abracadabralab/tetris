import pygame as pg
import numpy as np


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

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.shape = np.rot90(self.shape, 1)
                
