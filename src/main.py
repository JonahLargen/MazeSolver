from cell import Cell
from point import Point
from line import Line
from window import Window

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50, 50), Point(100, 100)), "red")
    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(200, 300, 300, 400)
    win.wait_for_close()

main()