from point import Point
from line import Line


class Cell:
    def __init__(self, win=None):
        self.__win = win
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._visited = False
        
    def draw(self, x1, y1, x2, y2):
        if (self.__win is None):
            return
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black" if self.has_left_wall else "white")
        self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black" if self.has_right_wall else "white")
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black" if self.has_top_wall else "white")
        self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black" if self.has_bottom_wall else "white")
            
    def draw_move(self, to_cell, undo=False):
        if (self.__win is None):
            return
        self.__win.draw_line(Line(Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2), Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)), "gray" if not undo else "red")