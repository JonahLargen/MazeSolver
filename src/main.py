from window import Window
from maze import Maze

def main():
    width = 800
    height = 600
    margin = 100
    cell_size = 50
    delay = 0.025
    win = Window(width, height)
    num_rows = (height - margin * 2) // cell_size
    num_cols = (width - margin * 2) // cell_size
    maze = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size, delay, win)
    win.wait_for_close()

main()