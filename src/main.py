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
    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(300, 300, 400, 400)
    cell.draw_move(cell2)
    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.draw(400, 400, 500, 500)
    cell2.draw_move(cell3, True)
    win.wait_for_close()

main()