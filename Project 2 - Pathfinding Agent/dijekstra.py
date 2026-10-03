# Dijkstra's Algorithm Implementation

# Functions in the code:
# valid_moves() - Checks if a move is valid (within bounds and not an obstacle)
# next_moves() - Returns a list of valid moves from the current position
# dijkstra() - Implementation of Dijkstra's algorithm

import heapq

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
    elif col < 0 or col >= len(grid[0]): # col out of bounds check
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

def reconstruct_path(parents):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parents[current]

    path.append(start)
    path.reverse()

    return path

def dijkstra():
    priority_queue = []

    heapq.heappush(priority_queue, (0, start))

    distances = {
        start: 0
    }

    parents = {}

    expanded_nodes = 0

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)
        expanded_nodes += 1

        if current == goal:
            break

        for neighbor in next_moves(current):
            new_cost = current_cost + 1

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parents[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor)
                )

    return distances, parents, expanded_nodes

def print_grid(path):
    path = set(path)

    for row in range(len(grid)):
        row_output = ""

        for col in range(len(grid[0])):

            position = (row, col)

            if position == start:
                row_output += "S "

            elif position == goal:
                row_output += "G "

            elif grid[row][col] == 1:
                row_output += "# "

            elif position in path:
                row_output += "* "

            else:
                row_output += ". "

        print(row_output)

def main():
    distances, parents, expanded_nodes = dijkstra()

    path = reconstruct_path(parents)

    print("Distance to goal:", distances.get(goal))
    print("Expanded nodes:", expanded_nodes)
    print("Path:", path)

    print("\nDijkstra Path:")
    print_grid(path)

main()