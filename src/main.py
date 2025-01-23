from window import Window
from maze import Maze
import sys

sys.setrecursionlimit(100_000)

def main():
    width = 1200
    height = 900
    margin = 100
    cell_size = 50
    delay = 0.02
    win = Window(width, height)
    num_rows = (height - margin * 2) // cell_size
    num_cols = (width - margin * 2) // cell_size
    maze = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size, delay, win, 0)
    maze.solve()
    print('Solved')
    win.wait_for_close()

main()