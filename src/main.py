from window import Window
from maze import Maze
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some command line arguments.")
    
    parser.add_argument('--width', type=int, default=800, help='Width in pixels')
    parser.add_argument('--height', type=int, default=600, help='Height in pixels')
    parser.add_argument('--margin', type=int, default=50, help='Margin in pixels')
    parser.add_argument('--size', type=int, default=100, help='Cell size in pixels')
    parser.add_argument('--delay', type=float, default=0.05, help='Base delay in seconds (will be scaled during different processes)')
    parser.add_argument('--seed', type=int, default=None, help='Seed used in random.seed(...)')
    parser.add_argument('--max_recursion', type=int, default=10_000, help='Max recursion for DFS')
    
    args = parser.parse_args()
    
    width = args.width
    height = args.height
    margin = args.margin
    cell_size = args.size
    delay =args.delay
    seed = args.seed
    max_recursion = args.max_recursion
    
    sys.setrecursionlimit(max_recursion)
    
    win = Window(width, height)
    num_rows = (height - margin * 2) // cell_size
    num_cols = (width - margin * 2) // cell_size
    maze = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size, delay, win, seed)
    maze.solve()
    win.wait_for_close()

main()