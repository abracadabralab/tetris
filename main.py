import os
from random import choice
import pygame as pg
from block import Block


class Window:
    def __init__(self, size: tuple, fps: int = 3):
        self.screen_size: tuple[int, int] = size
        self.display = pg.display.set_mode(size)

        self.clock = pg.time.Clock()
        self.fps: int = fps
        self.run: bool = True
        self.game_over: bool = False

        self.blocks: list = []
        self.current_block: Block = None
        self.grid: list[list] = [[0] * 17 for _ in range(int(size[1] / 20))]

        self.step: int = 20
        self.shift = 9
        self.block_level: int = 0

        self.lines = 0
        self.level = 1
        self.score = 0

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

            self.block_check()

            if self.current_block.can_fall():
                self.current_block.fall()
                self.current_block.block_level += 1
            else:
                self.score += self.level * 30
                self.block_level = 0
                self.blocks.append(Block(choice([*range(1, 7)]), self.grid, self.screen_size))
                self.current_block = self.blocks[-1]
                self.current_block.add_to_grid()

            self.draw_grid()
            self.blit_text()

            if self.current_block.game_over:
                self.game_over_screen()

            pg.display.flip()
            self.clock.tick(self.fps + self.current_block.speed + self.level)

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

    def block_check(self):
        if self.lines % 10 == 0 and self.lines != 0:
            self.level += 1
            self.lines = 0

        for i in range(len(self.grid)):
            if 0 not in self.grid[i]:
                self.grid.remove(self.grid[i])
                self.grid.insert(0, ([0] * 17))
                self.lines += 1

    def blit_text(self):
        pg.init()

        main_font = pg.font.Font(os.path.join("assets/pixel.ttf"), 30)
        level_label = main_font.render(f"LEVEL: {self.level}", True, "white")
        score_label = main_font.render(f"SCORE: {self.score}", True, "white")

        self.display.blit(level_label, (self.screen_size[0] - level_label.get_width() - 10, 20))
        self.display.blit(score_label, (self.screen_size[0] - score_label.get_width() - 10, 50))

    def start_screen(self):
        pg.init()

        logo = pg.image.load(os.path.join("assets/logo.png"))
        logo = pg.transform.scale(logo, (logo.get_width() / 2.5, logo.get_height() / 2.5))

        tetris_font = pg.font.Font(os.path.join("assets/pixel.ttf"), 100)
        start_label = tetris_font.render("START", True, "white")

        while self.run:
            self.display.fill("black")
            self.display.blit(logo, (self.screen_size[0] / 2 - logo.get_width() / 2,
                                     self.screen_size[1] / 4 - logo.get_height() / 2))
            self.display.blit(start_label, (self.screen_size[0] / 2 - start_label.get_width() / 2,
                                            self.screen_size[1] / 3 * 2 - start_label.get_height() / 2))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                    if event.key == pg.K_SPACE:
                        self.start()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    if self.screen_size[0] / 2 - start_label.get_width() / 2 <= mouse[0] <= \
                            self.screen_size[0] / 2 + start_label.get_width() / 2 and \
                            self.screen_size[1] / 3 * 2 - start_label.get_height() / 2 <= mouse[1] <= \
                            self.screen_size[1] / 3 * 2 + start_label.get_height() / 2:
                        self.start()
            pg.display.flip()

    def game_over_screen(self):
        pg.init()

        tetris_font = pg.font.Font(os.path.join("assets/pixel.ttf"), 100)
        secondary_font = pg.font.SysFont("Tahoma", 30)

        game_over_label = tetris_font.render("GAME OVER", True, "white")
        instructions = secondary_font.render("to start over press SPACE", True, "white")

        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                    if event.key == pg.K_SPACE:
                        new_window = Window((700, 520))
                        new_window.start()
            self.display.fill("black")
            self.display.blit(game_over_label, (self.screen_size[0] / 2 - game_over_label.get_width() / 2,
                                                self.screen_size[1] / 2 - game_over_label.get_height() / 2))
            self.display.blit(instructions, (self.screen_size[0] / 2 - instructions.get_width() / 2,
                                             self.screen_size[1] / 2 + 100 - instructions.get_height() / 2))
            pg.display.flip()


def main():
    window = Window((700, 520))
    window.start_screen()


if __name__ == '__main__':
    main()
