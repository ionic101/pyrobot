import tkinter as tk
from settings import *
from robot import Robot
from direction import Direction


class Game:
    def __init__(self, root: tk.Tk, screen_size: tuple[int], cells: list[list[str]]) -> None:
        self.root = root

        self.canvas = tk.Canvas(root, width=screen_size[0], height=screen_size[1], bg='white')
        self.canvas.pack()

        self.robot = Robot(root, cells, self.update_screen)

    def draw_cell(self, x: int, y: int, cell_color: str) -> None:
        x *= CELL_SCALE
        y *= CELL_SCALE
        self.canvas.create_rectangle(x, y, x + CELL_SCALE, y + CELL_SCALE, fill=cell_color)
    
    def draw_robot(self, x: int, y: int, direction: Direction) -> None:
        x *= CELL_SCALE
        y *= CELL_SCALE
        offset = CELL_SCALE * (1 - ROBOT_SCALE) // 2
        self.canvas.create_oval(
            x + offset,
            y + offset,
            x + CELL_SCALE - offset,
            y + CELL_SCALE - offset, fill=ROBOT_COLOR)
        
        self.canvas.create_line(
            x + CELL_SCALE // 2,
            y + CELL_SCALE // 2,
            x + CELL_SCALE // 2 + direction.x * CELL_SCALE // 2,
            y + CELL_SCALE // 2 + direction.y * CELL_SCALE // 2,
            width=ARROW_WIDTH,
            fill=ARROW_COLOR,
            arrow=tk.LAST)

    def draw_background(self, cells: list[list[str]]) -> None:
        for y, line in enumerate(cells):
            for x, cell in enumerate(line):
                self.draw_cell(x, y, COLORS[cell])

    def update_screen(self, cells: list[list[str]], robot_coords: tuple[int], robot_dir: Direction) -> None:
        self.canvas.delete('all')
        self.draw_background(cells)
        self.draw_robot(*robot_coords, robot_dir)
