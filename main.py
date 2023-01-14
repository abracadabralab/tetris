import os
from random import choice
import pygame as pg
from block import Block


class Window:
    def __init__(self, size: tuple, fps: int = 5):
        self.screen_size: tuple[int, int] = size
        self.display = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.fps: int = fps
        self.run: bool = True
        self.blocks: list = []
        self.current_block: Block = None
        self.grid: list[list] = [[0] * 17 for _ in range(int(size[1] / 20))]

        self.step: int = 20
        self.shift = 9
        self.block_level: int = 0

        self.level = 1
        self.lines = 0

    def start(self):
        self.blocks.append(Block(choice([*range(1, 7)]), self.grid, self.screen_size))
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

            if self.current_block.can_fall(self.lines):
                self.lines = self.current_block.lines
                print(self.lines)
                self.current_block.fall()
                self.current_block.block_level += 1
            else:
                self.block_level = 0
                self.blocks.append(Block(choice([*range(1, 7)]), self.grid, self.screen_size))
                self.current_block = self.blocks[-1]
                self.current_block.add_to_grid()

            self.draw_grid()

            pg.display.flip()
            self.clock.tick(self.fps + self.current_block.speed)

    def draw_grid(self):
        self.draw_grid_lines()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != 0:
                    rect = pg.Rect((2 * self.shift * self.step + self.step * j - self.shift * self.step, self.step * i),
                                   (self.step, self.step))
                    pg.draw.rect(self.display, str(self.grid[i][j]), rect)

    def draw_grid_lines(self):
        for i in range(self.step, self.screen_size[0], self.step):
            pg.draw.line(self.display, "#3a3b3c", (self.shift * self.step, i),
                         (self.screen_size[0] - self.shift * self.step, i))

        for j in range(self.shift * self.step, self.screen_size[0] - self.shift * self.step + 1, self.step):
            pg.draw.line(self.display, "#3a3b3c", (j, 0), (j, self.screen_size[0]))

    # def level(self):
    #     self.display.blit(self.display, )

    def start_menu(self):
        pg.init()

        logo = pg.image.load(os.path.join("logo.png"))
        logo = pg.transform.scale(logo, (logo.get_width()/2.5, logo.get_height()/2.5))

        tetris_font = pg.font.Font(os.path.join("pixel.ttf"), 100)
        start_label = tetris_font.render("START", True, "white")

        while self.run:
            self.display.fill("black")
            self.display.blit(logo, (self.screen_size[0]/2 - logo.get_width()/2,
                                     self.screen_size[1]/4 - logo.get_height()/2))
            self.display.blit(start_label, (self.screen_size[0]/2 - start_label.get_width()/2,
                                            self.screen_size[1]/3 * 2 - start_label.get_height()/2))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                    if event.key == pg.K_SPACE:
                        self.start()
                        print("true")
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    if self.screen_size[0]/2 - start_label.get_width()/2 <= mouse[0] <= \
                            self.screen_size[0]/2 + start_label.get_width()/2 and \
                            self.screen_size[1]/3 * 2 - start_label.get_height()/2 <= mouse[1] <= \
                            self.screen_size[1]/3 * 2 + start_label.get_height()/2:
                        self.start()
            pg.display.flip()


def main():
    width, height = 700, 520
    window = Window((width, height))
    window.start_menu()


if __name__ == '__main__':
    main()
