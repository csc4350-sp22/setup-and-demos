"""
Borrowed from domoritz at https://github.com/domoritz/gameoflife-python
"""
from collections import namedtuple, defaultdict
import time

Cell = namedtuple("Cell", ["x", "y"])
pad = 2
def getNeighbors(cell):
    for x in range(cell.x-1, cell.x+2):
        for y in range(cell.y-1, cell.y+2):
            if (x,y) != (cell.x, cell.y):
                yield Cell(x,y)
def advanceBoard(board):
    new_board = set()
    neighbor_counts = defaultdict(int)
    for cell in board:
        for neighbor in getNeighbors(cell):
            neighbor_counts[neighbor]+=1
    for cell, count in neighbor_counts.items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)
    return new_board    
if __name__ == "__main__":
    desc = "......X.\nXX......\n.X...XXX"
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == "X":
                board.add(Cell(int(col), int(row)))
    f = board

    for _ in range(130):
        f = advanceBoard(f)

        if not f:
             board_string = "empty"
        else:
            board_str = ""
            xs = [x for (x, _) in f]
            ys = [y for (_, y) in f]
            for y in range(min(ys) - pad, max(ys) + 1 + pad):
                for x in range(min(xs) - pad, max(xs) + 1 + pad):
                    board_str += "X" if Cell(x, y) in f else "."
                board_str += "\n"
            board_string = board_str.strip()

        print("\033[2J\033[1;1H" + board_string)
        time.sleep(0.1)
