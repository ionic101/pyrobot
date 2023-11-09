import direction
from settings import *
import tkinter as tk

class Robot:
    def __init__(self, root: tk.Tk, cells: list[list[str]], update_screen_func) -> None:
        self.root = root
        self.cells = cells
        self.update_screen_func = update_screen_func

        self.direction = ROBOT_START_DIRECTION
        self.x, self.y = self.get_robot_coords()

        self.tick = 0
        self.update_screen()

    def update_screen(self) -> None:
        def get_cells(cells: list[list[str]]) -> list[list[str]]:
            new_cells = []
            for line in cells:
                new_cells.append(line.copy())
            
            return new_cells
        
        self.root.after(DELAY * self.tick, self.update_screen_func, get_cells(self.cells), (self.x, self.y), self.direction)
        self.tick += 1
    
    def get_robot_coords(self) -> tuple[int]:
        for y, line in enumerate(self.cells):
            for x, cell in enumerate(line):
                if cell == 'r':
                    self.cells[y][x] = '*'
                    return x, y
        else:
            raise "Robot doesnt found!"

    def move(self) -> None:
        new_x = self.x + self.direction.x
        new_y = self.y + self.direction.y

        if self.cells[new_y][new_x] == '#':
            pass
        else:
            if self.cells[new_y][new_x] not in 'gp':
                self.cells[new_y][new_x] = '*'
            self.x = new_x
            self.y = new_y
        
        self.update_screen()
    
    def check_garden_under(self) -> bool:
        return self.cells[self.y][self.x] == 'g'
    
    def check_wall_ahead(self) -> bool:
        return self.cells[self.y + self.direction.y][self.x + self.direction.x] == '#'

    def turn_left(self) -> None:
        if self.direction == direction.Up:
            self.direction = direction.Left
        elif self.direction == direction.Left:
            self.direction = direction.Down
        elif self.direction == direction.Down:
            self.direction = direction.Right
        elif self.direction == direction.Right:
            self.direction = direction.Up
        
        self.update_screen()

    def turn_right(self) -> None:
        if self.direction == direction.Up:
            self.direction = direction.Right
        elif self.direction == direction.Right:
            self.direction = direction.Down
        elif self.direction == direction.Down:
            self.direction = direction.Left
        elif self.direction == direction.Left:
            self.direction = direction.Up
        
        self.update_screen()

    def plant(self) -> None:
        self.cells[self.y][self.x] = 'p'

        self.update_screen()
