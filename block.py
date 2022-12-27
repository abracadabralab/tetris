import pygame as pg
import numpy as np


ORANGE_RICKY = [
    [False, False, False],
    [False, False, True],
    [True, True, True]
]
BLUE_RICKY = [
    [False, False, False],
    [True, False, False],
    [True, True, True]
]
CLEVELAND_Z = [
    [False, False, False],
    [True, True, False],
    [False, True, True]
]
RHODE_ISLAND_Z = [
    [False, False, False],
    [False, True, True],
    [True, True, False]
]
HERO = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [True, True, True, True]
]
TEEWEE = [
    [False, False, False],
    [False, True, False],
    [True, True, True]
]
SMASHBOY = [
    [False, False, False],
    [True, True, False],
    [True, True, False]
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
                    pg.draw.rect(display, "white", rect)

    def handle_event(self, event):
        directions = {
            pg.K_LEFT: 1,
            pg.K_RIGHT: -1,
        }
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_LEFT, pg.K_RIGHT]:
                self.shape = np.rot90(self.shape, directions[event.key])
