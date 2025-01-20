from point import Point
from line import Line


class Cell:
    def __init__(self, win):
        self.__win = win
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
            
    def draw_move(self, to_cell, undo=False):
        self.__win.draw_line(Line(Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2), Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)), "gray" if not undo else "red")