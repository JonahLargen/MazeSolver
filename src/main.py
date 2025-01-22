from window import Window
from maze import Maze

def main():
    win = Window(1800, 1200)
    maze = Maze(600, 600, 3, 4, 50, 50, win)
    win.wait_for_close()

main()