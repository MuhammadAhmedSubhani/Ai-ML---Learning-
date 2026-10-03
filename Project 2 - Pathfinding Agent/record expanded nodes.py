# Maze 1 → Simple
# Maze 2 → More obstacles
# Maze 3 → Dense obstacles
# Maze 4 → Larger grid
# Maze 5 → Different obstacle layout

# Functions in the code:
# valid_moves() - Checks if a move is valid (within bounds and not an obstacle)
# next_moves() - Returns a list of valid moves from the current position
# dijkstra() - Implementation of Dijkstra's algorithm
# a_star() - Implementation of the A* algorithm
# Benchmark() - Runs both algorithms on all mazes and prints results
# Maze - Added NOW

import heapq
import time

grid = [
    [0, 0, 0, 1, 0],   # 0 = walkable 
    [0, 1, 0, 1, 0],   # 1 = obstacle 
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

mazes = [
    {
        "name": "Maze 1 - Simple",
        "grid": [
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    },

    {
        "name": "Maze 2 - More Obstacles",
        "grid": [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    },

    {
        "name": "Maze 3 - Dense Obstacles",
        "grid": [
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    },

    {
        "name": "Maze 4 - Larger 10x10 Grid",
        "grid": [
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0]
        ],
        "start": (0, 0),
        "goal": (9, 9)
    },

    {
        "name": "Maze 5 - Different Layout",
        "grid": [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    },

    {
            "name": "Maze 6 - Fail grid",
            "grid": [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]
            ],
            "start": (0, 0),
            "goal": (4, 4)
    }
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

    # Check if the goal was reached
    if current != start and current not in parents:
        return []

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

def print_search_visualization(expanded_nodes, path):
    expanded_nodes = set(expanded_nodes)
    path = set(path)

    print()

    for row in range(len(grid)):
        row_output = ""

        for col in range(len(grid[0])):

            position = (row, col)

            if position == start:
                row_output += "S " # S = Start
            elif position == goal:
                row_output += "G " # G = Goal
            elif grid[row][col] == 1:
                row_output += "# "   # # = Obstacle
            elif position in path:
                row_output += "* " # * = Path
            elif position in expanded_nodes:
                row_output += "E " # E = Expanded
            else:
                row_output += ". "  # . = Unvisited walkable cell

        print(row_output)

def dijkstra():
    priority_queue = []

    heapq.heappush(priority_queue, (0, start))

    distances = {start: 0}
    parents = {}

    # Store every node that Dijkstra expands
    expanded_nodes = []

    while priority_queue:

        current_cost, current = heapq.heappop(priority_queue)

        # Ignore outdated queue entries
        if current_cost != distances[current]:
            continue

        # Record this node as expanded
        expanded_nodes.append(current)

        # Stop when goal is reached
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

    distances = {start: 0}
    parents = {}

    # Store every node that A* expands
    expanded_nodes = []

    while priority_queue:

        current_f, current = heapq.heappop(priority_queue)

        current_g = distances[current]
        expected_f = current_g + heuristic(current)

        # Ignore outdated queue entries
        if current_f != expected_f:
            continue

        # Record this node as expanded
        expanded_nodes.append(current)

        # Stop when goal is reached
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

    global grid, start, goal

    for maze_number, maze in enumerate(mazes, start=1):

        # Load the current maze
        grid = maze["grid"]
        start = maze["start"]
        goal = maze["goal"]

        print("\n==============================")
        print(maze["name"])
        print("==============================")

        # -------------------------
        # Run Dijkstra
        # -------------------------

        start_time = time.perf_counter()

        distances_dijkstra, parents_dijkstra, expanded_dijkstra = dijkstra()

        dijkstra_time = time.perf_counter() - start_time

        dijkstra_path = reconstruct_path(parents_dijkstra)

        # -------------------------
        # Run A*
        # -------------------------

        start_time = time.perf_counter()

        distances_a_star, parents_a_star, expanded_a_star = a_star()

        a_star_time = time.perf_counter() - start_time

        a_star_path = reconstruct_path(parents_a_star)

        # -------------------------
        # Calculate densities
        # -------------------------

        dijkstra_density = expanded_node_density(
            len(expanded_dijkstra)
        )

        a_star_density = expanded_node_density(
            len(expanded_a_star)
        )

        # -------------------------
        # Display Dijkstra results
        # -------------------------

        print("\nDijkstra:")

        if dijkstra_path:
            print("Path length:", len(dijkstra_path) - 1)
        else:
            print("No path found.")

        print("Expanded nodes:", len(expanded_dijkstra))
        print("Runtime:", dijkstra_time, "seconds")
        print(
            "Expanded node density:",
            round(dijkstra_density, 2),
            "%"
        )

        # -------------------------
        # Display A* results
        # -------------------------

        print("\nA*:")

        if a_star_path:
            print("Path length:", len(a_star_path) - 1)
        else:
            print("No path found.")

        print("Expanded nodes:", len(expanded_a_star))
        print("Runtime:", a_star_time, "seconds")
        print(
            "Expanded node density:",
            round(a_star_density, 2),
            "%"
        )

def visualize_maze(maze_index):

    global grid, start, goal

    # Load selected maze
    maze = mazes[maze_index]

    grid = maze["grid"]
    start = maze["start"]
    goal = maze["goal"]

    print("\n==============================")
    print(maze["name"])
    print("==============================")

    # -------------------------
    # Dijkstra visualization
    # -------------------------

    distances_dijkstra, parents_dijkstra, expanded_dijkstra = dijkstra()

    dijkstra_path = reconstruct_path(parents_dijkstra)

    print("\n===== DIJKSTRA SEARCH =====")

    if dijkstra_path:
        print("Path length:", len(dijkstra_path) - 1)
    else:
        print("No path found.")

    print_search_visualization(
        expanded_dijkstra,
        dijkstra_path
    )

    # -------------------------
    # A* visualization
    # -------------------------

    distances_a_star, parents_a_star, expanded_a_star = a_star()

    a_star_path = reconstruct_path(parents_a_star)

    print("\n===== A* SEARCH =====")

    if a_star_path:
        print("Path length:", len(a_star_path) - 1)
    else:
        print("No path found.")

    print_search_visualization(
        expanded_a_star,
        a_star_path
    )

def save_visualization(maze_index):

    global grid, start, goal

    maze = mazes[maze_index]

    grid = maze["grid"]
    start = maze["start"]
    goal = maze["goal"]

    filename = f"maze_{maze_index + 1}_visualization.txt"

    with open(filename, "w") as file:

        file.write("==============================\n")
        file.write(maze["name"] + "\n")
        file.write("==============================\n\n")

        # Dijkstra

        distances_dijkstra, parents_dijkstra, expanded_dijkstra = dijkstra()

        dijkstra_path = reconstruct_path(parents_dijkstra)

        file.write("===== DIJKSTRA SEARCH =====\n")

        if dijkstra_path:
            file.write(
                f"Path length: {len(dijkstra_path) - 1}\n\n"
            )
        else:
            file.write("No path found.\n\n")

        expanded_set = set(expanded_dijkstra)
        path_set = set(dijkstra_path)

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

                elif position in path_set:
                    row_output += "* "

                elif position in expanded_set:
                    row_output += "E "

                else:
                    row_output += ". "

            file.write(row_output + "\n")

        file.write("\n")

        # A*

        distances_a_star, parents_a_star, expanded_a_star = a_star()

        a_star_path = reconstruct_path(parents_a_star)

        file.write("===== A* SEARCH =====\n")

        if a_star_path:
            file.write(
                f"Path length: {len(a_star_path) - 1}\n\n"
            )
        else:
            file.write("No path found.\n\n")

        expanded_set = set(expanded_a_star)
        path_set = set(a_star_path)

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

                elif position in path_set:
                    row_output += "* "

                elif position in expanded_set:
                    row_output += "E "

                else:
                    row_output += ". "

            file.write(row_output + "\n")

    print(f"\nVisualization saved: {filename}")    

benchmark()
visualize_maze(3)
save_visualization(3)