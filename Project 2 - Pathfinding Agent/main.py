grid = [
    [0, 0, 0, 1, 0],   # 0 = walkable 
    [0, 1, 0, 1, 0],   # 1 = obstacle 
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4,4)

def moves( row, col ):
    if row < 0 or row >= len(grid): # row out of bounds check
        return False
    elif col < 0 or col >= len(grid): # col out of bounds check
        return False
    elif grid[row][col] == 1: # Obstacle detection
        return False
    else:
        return True
def main():
    print(moves(0, 0))
    print(moves(1, 1))
    print(moves(5, 5))

main()