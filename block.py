import pygame as pg
import numpy as np
from dataclasses import dataclass
from enum import Enum
from pygame.math import Vector2
from random import choice
from pygame.surface import Surface


@dataclass
class Shape:
    color: str
    points: list[Vector2]


ORANGE_RICKY = [
    Vector2(0, 40),
    Vector2(60, 40),
    Vector2(60, 0),
    Vector2(40, 0),
    Vector2(40, 20),
    Vector2(0, 20),
    Vector2(0, 40),
]
BLUE_RICKY = [
    Vector2(0, 40),
    Vector2(60, 40),
    Vector2(60, 20),
    Vector2(20, 20),
    Vector2(20, 0),
    Vector2(0, 0),
    Vector2(0, 40),
]
CLEVELAND_Z = [
    Vector2(0, 0),
    Vector2(0, 20),
    Vector2(20, 20),
    Vector2(20, 40),
    Vector2(60, 40),
    Vector2(60, 20),
    Vector2(40, 20),
    Vector2(40, 0),
    Vector2(0, 0),
]
RHODE_ISLAND_Z = [
    Vector2(0, 40),
    Vector2(40, 40),
    Vector2(40, 20),
    Vector2(60, 20),
    Vector2(60, 0),
    Vector2(20, 0),
    Vector2(20, 20),
    Vector2(0, 20),
    Vector2(0, 40),
]
HERO = [
    Vector2(0, 0),
    Vector2(0, 20),
    Vector2(80, 20),
    Vector2(80, 0),
    Vector2(0, 0),
]
TEEWEE = [
    Vector2(0, 40),
    Vector2(60, 40),
    Vector2(60, 20),
    Vector2(40, 20),
    Vector2(40, 0),
    Vector2(20, 0),
    Vector2(20, 20),
    Vector2(0, 20),
    Vector2(0, 40),
]
SMASHBOY = [
    Vector2(0, 0),
    Vector2(0, 40),
    Vector2(40, 40),
    Vector2(40, 0),
    Vector2(0, 0),
]
SHAPES = [
    Shape("orange", ORANGE_RICKY),
    Shape("blue", BLUE_RICKY),
    Shape("red", CLEVELAND_Z),
    Shape("green", RHODE_ISLAND_Z),
    Shape("cyan", HERO),
    Shape("purple", TEEWEE),
    Shape("yellow", SMASHBOY),
]


class Direction(Enum):
    RIGHT = 1
    LEFT = 2


class Block(pg.sprite.Sprite):
    def __init__(self, shape: Shape):
        super().__init__()
        self.shape: Shape = shape
        self.step: int = 20
        self.speed = 2
        self.pos: Vector2 = Vector2(20, 20)
        self.surface: Surface = Surface((80, 80), pg.SRCALPHA, 32).convert_alpha()
        self.rect = pg.draw.polygon(self.surface, self.shape.color, self.shape.points)

    def draw(self, display: Surface):
        display.blit(self.surface, self.pos, self.rect)

    def fall(self):
        self.pos.y += self.speed

    def handle_event(self, event) -> None:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.__rotate()
            if event.key == pg.K_RIGHT:
                self.__move(Direction.RIGHT)
            if event.key == pg.K_LEFT:
                self.__move(Direction.LEFT)
            if event.key == pg.K_SPACE:
                self.__inc_speed()
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                self.__dec_speed()

    def __rotate(self) -> None:
        self.surface = pg.transform.rotate(self.surface, 90)
        self.rect = self.surface.get_rect()

    def __move(self, direction: Direction) -> None:
        match direction:
            case Direction.RIGHT:
                self.pos.x += self.step
            case Direction.LEFT:
                self.pos.x -= self.step

    def __inc_speed(self):
        self.speed *= 3

    def __dec_speed(self):
        self.speed /= 3
