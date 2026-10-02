grid = [
    [0, 0, 0, 1, 0],   # 0 = walkable 
    [0, 1, 0, 1, 0],   # 1 = obstacle 
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4,4)

def valid_moves( row, col ):
    if row < 0 or row >= len(grid): # row out of bounds check
        return False
    elif col < 0 or col >= len(grid): # col out of bounds check
        return False
    elif grid[row][col] == 1: # Obstacle detection
        return False
    else:
        return True

def next_moves(pos):
    row,col = pos
    directions = [
        (-1,0), #Up
        (1,0), # Down
        (0,-1), #Left
        (0, 1) #Right
    ]
    move = []
    for row_change, col_change in directions:
        new_row = row + row_change
        new_col = col + col_change

        if valid_moves(new_row, new_col):
            move.append((new_row, new_col))

    return move


def main():
    print("Neighbors of start:", next_moves(start))

main()