import heapq
import time

grid = [
    [0, 0, 0, 1, 0],   # 0 = walkable 
    [0, 1, 0, 1, 0],   # 1 = obstacle 
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4,4)

def valid_moves(row, col):
    if row < 0 or row >= len(grid):
        return False
    elif col < 0 or col >= len(grid[0]):
        return False
    elif grid[row][col] == 1:
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

def heuristic(position):
    row, col = position
    goal_row, goal_col = goal

    return abs(row - goal_row) + abs(col - goal_col)

def a_star():
    priority_queue = []
    start_g = 0
    start_h = heuristic(start)
    start_f = start_g + start_h
    heapq.heappush(priority_queue, (start_f, start))

    distances = {
        start: 0
    }

    parents = {}

    expanded_nodes = 0

    while priority_queue:
        current_f, current = heapq.heappop(priority_queue)

        # Calculate the actual g-cost represented by this queue entry
        current_g = distances[current]

        # Ignore outdated queue entries
        expected_f = current_g + heuristic(current)

        if current_f != expected_f:
            continue

        expanded_nodes += 1

        if current == goal:
            break

        for neighbor in next_moves(current):
            new_g = current_g + 1

            if neighbor not in distances or new_g < distances[neighbor]:
                distances[neighbor] = new_g
                parents[neighbor] = current
                h = heuristic(neighbor)
                f = new_g + h

                heapq.heappush(
                    priority_queue,
                    (f, neighbor)
                )

    return distances, parents, expanded_nodes

def expanded_node_density(expanded_nodes): # counts the number of expanded nodes and divides it by the total number of walkable nodes in the grid to get a percentage
    total_walkable = 0

    for row in grid:
        for cell in row:
            if cell == 0:
                total_walkable += 1

    return (expanded_nodes / total_walkable) * 100

def benchmark():
    # Run Dijkstra
    start_time = time.perf_counter()

    distances_dijkstra, parents_dijkstra, expanded_dijkstra = dijkstra()

    dijkstra_time = time.perf_counter() - start_time

    dijkstra_path = reconstruct_path(parents_dijkstra)

    # Run A*
    start_time = time.perf_counter()

    distances_a_star, parents_a_star, expanded_a_star = a_star()

    a_star_time = time.perf_counter() - start_time

    a_star_path = reconstruct_path(parents_a_star)
    dijkstra_density = expanded_node_density(expanded_dijkstra)
    a_star_density = expanded_node_density(expanded_a_star)

    # Print results
    print("\nDijkstra:")
    print("Path length:", len(dijkstra_path) - 1)
    print("Expanded nodes:", expanded_dijkstra)
    print("Runtime:", dijkstra_time, "seconds")
    print("Expanded node density:", dijkstra_density, "%")

    print("\nA*:")
    print("Path length:", len(a_star_path) - 1)
    print("Expanded nodes:", expanded_a_star)
    print("Runtime:", a_star_time, "seconds")
    print("Expanded node density:", a_star_density, "%")

benchmark()
