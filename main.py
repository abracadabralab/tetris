from random import choice
import pygame as pg
from block import Block, BLOCKS


class Window:
    def __init__(self, size: tuple, fps: int = 60):
        self.display = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.run = True
        self.blocks = []

    def start(self):
        self.blocks.append(Block(shape=choice(BLOCKS)))

        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                for block in self.blocks:
                    block.handle_event(event)

            self.display.fill("black")

            for block in self.blocks:
                block.draw(self.display)

            pg.display.flip()
            self.clock.tick(self.fps)


def main():
    window = Window((1280, 720))
    window.start()


if __name__ == '__main__':
    main()