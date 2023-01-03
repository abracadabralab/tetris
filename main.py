from random import choice
import pygame as pg
from block import Block, SHAPES


class Window:
    def __init__(self, size: tuple, fps: int = 5):
        self.screen_size: tuple[int, int] = size
        self.display = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.fps: int = fps
        self.run: bool = True
        self.blocks: list = []
        self.current_block: Block = None
        self.grid: list[list] = [[None] * int(size[0] / 20) for _ in range(int(size[1] / 20))]
        self.step: int = 20
        self.block_level: int = 0

    def start(self):
        self.blocks.append(Block(choice(SHAPES), self.grid, self.screen_size))
        self.current_block = self.blocks[-1]
        self.current_block.add_to_grid()

        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                self.current_block.handle_event(event)

            self.display.fill("black")

            if self.block_level <= (self.screen_size[1]/self.step - 3):
                self.current_block.fall(self.block_level)
                self.block_level += 1
            else:
                self.block_level = 0
                self.blocks.append(Block(choice(SHAPES), self.grid, self.screen_size))
                self.current_block = self.blocks[-1]
                self.current_block.add_to_grid()

            self.draw_grid()

            pg.display.flip()
            self.clock.tick(self.fps)

    def draw_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]:
                    rect = pg.Rect((self.step * j, self.step * i), (self.step, self.step))
                    pg.draw.rect(self.display, "purple", rect)


def main():
    width, height = 700, 520
    window = Window((width, height))
    window.start()


if __name__ == '__main__':
    main()
