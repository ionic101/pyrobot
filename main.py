import tkinter as tk
from settings import *
from game import Game
from read_level import read_level
import script
from threading import Thread

cells = read_level(LEVEL_FILE_NAME)
screen_size = (len(cells[0]) * CELL_SCALE, len(cells) * CELL_SCALE)

root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry(f'{screen_size[0]}x{screen_size[1]}')
root.resizable(False, False)

game = Game(root, screen_size, cells)

script_thread = Thread(target=script.robot_behavior_tree, args=[game.robot])
script_thread.start()

root.mainloop()
