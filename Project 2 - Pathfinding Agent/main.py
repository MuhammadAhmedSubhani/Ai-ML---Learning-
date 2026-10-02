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

def main():
    distances, parents, expanded_nodes = dijkstra()

    print("Distance to goal:", distances.get(goal))
    print("Expanded nodes:", expanded_nodes)
    print("Parents:", parents)

main()