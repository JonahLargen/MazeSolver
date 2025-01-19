from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.widget = Canvas(self.root, height=height, width=width, bg='white')
        self.widget.pack(fill=BOTH, expand=True)
        self.running = False

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False