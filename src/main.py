from window import Window
from maze import Maze
import sys

sys.setrecursionlimit(100_000)

def main():
    width = 2500
    height = 2000
    margin = 100
    cell_size = 25
    delay = 0.0001
    win = Window(width, height)
    num_rows = (height - margin * 2) // cell_size
    num_cols = (width - margin * 2) // cell_size
    maze = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size, delay, win, 0)
    win.wait_for_close()

main()