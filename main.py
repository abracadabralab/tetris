from random import choice
import pygame as pg
from block import Block, SHAPES


class Window:
    def __init__(self, size: tuple, fps: int = 60):
        self.display = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.run = True
        self.blocks: pg.sprite.Group = pg.sprite.Group()
        self.current_block: Block = None

    def start(self):
        self.blocks.add(self.new_block())
        self.current_block = self.blocks.sprites()[-1]

        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                    if event.key == pg.K_n:
                        self.blocks.add(self.new_block())
                        self.current_block = self.blocks.sprites()[-1]
                self.current_block.handle_event(event)

            self.display.fill("black")

            self.current_block.fall()
            for block in self.blocks:
                block.draw(self.display)

            pg.display.flip()
            self.clock.tick(self.fps)

    @staticmethod
    def new_block() -> Block:
        return Block(shape=choice(SHAPES))


def main():
    height, width = 720, 700
    window = Window((width, height))
    window.start()


if __name__ == '__main__':
    main()
