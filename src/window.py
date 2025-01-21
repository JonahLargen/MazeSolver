from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__widget = Canvas(self.__root, height=height, width=width, bg='white')
        self.__widget.pack(fill=BOTH, expand=True)
        self.__running = False

    def redraw(self):
        self.__widget.update_idletasks()
        self.__widget.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
            
    def close(self):
        self.__running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.__widget, fill_color)