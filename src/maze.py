from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, delay, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._delay = delay
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if (self._win is None):
            return
        self._cells[i][j].draw(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y, self._x1 + (i + 1) * self._cell_size_x, self._y1 + (j + 1) * self._cell_size_y)
        self._animate(scale=0.25)

    def _animate(self, scale=1):
        if (self._win is None):
            return
        self._win.redraw()
        time.sleep(self._delay * scale)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            l = []
            if i > 0:
                left = self._cells[i - 1][j]
                if not left.visited:
                    l.append((i - 1, j, 'left'))
            if i < self._num_cols - 1:
                right = self._cells[i + 1][j]
                if not right.visited:
                    l.append((i + 1, j, 'right'))
            if j > 0:
                top = self._cells[i][j - 1]
                if not top.visited:
                    l.append((i, j - 1, 'top'))
            if j < self._num_rows - 1:
                bottom = self._cells[i][j + 1]
                if not bottom.visited:
                    l.append((i, j + 1, 'bottom'))
            if len(l) == 0:
                self._draw_cell(i, j)
                self._animate()
                return
            random_index = random.randint(0, len(l) - 1)
            random_cell = l[random_index]
            i2 = random_cell[0]
            j2 = random_cell[1]
            type = random_cell[2]
            if type == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j2].has_right_wall = False
            elif type == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j2].has_left_wall = False
            elif type == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[i2][j2].has_bottom_wall = False
            elif type == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i2][j2].has_top_wall = False
            self._break_walls_r(i2, j2)
            
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                
    def solve(self):
        self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate(scale=3)
        cell = self._cells[i][j]
        cell.visited = True
        if cell == self._cells[-1][-1]:
            return True
        if i > 0:
            left = self._cells[i - 1][j]
            if not left.has_right_wall and not left.visited:
                cell.draw_move(left)
                solved = self._solve_r(i - 1, j)
                if solved:
                    return True
                else:
                    cell.draw_move(left, undo=True)
        if i < self._num_cols - 1:
            right = self._cells[i + 1][j]
            if not right.has_left_wall and not right.visited:
                cell.draw_move(right)
                solved = self._solve_r(i + 1, j)
                if solved:
                    return True
                else:
                    cell.draw_move(right, undo=True)
        if j > 0:
            top = self._cells[i][j - 1]
            if not top.has_bottom_wall and not top.visited:
                cell.draw_move(top)
                solved = self._solve_r(i, j - 1)
                if solved:
                    return True
                else:
                    cell.draw_move(top, undo=True)
        if j < self._num_rows - 1:
            bottom = self._cells[i][j + 1]
            if not bottom.has_top_wall and not bottom.visited:
                cell.draw_move(bottom)
                solved = self._solve_r(i, j + 1)
                if solved:
                    return True
                else:
                    cell.draw_move(bottom, undo=True)
        return False