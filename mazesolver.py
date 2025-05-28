# maze_solver.py

from collections import deque
import copy

# Define the maze
maze = [
    ['S', ' ', '#', ' ', 'E'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#']
]

ROWS = len(maze)
COLS = len(maze[0])
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def find_start():
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == 'S':
                return r, c
    return None

def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] != '#'

def bfs(start):
    queue = deque()
    queue.append((start, [start]))  # (current_position, path_so_far)
    visited = set()
    visited.add(start)

    while queue:
        (r, c), path = queue.popleft()

        if maze[r][c] == 'E':
            return path

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and (nr, nc) not in visited:
                queue.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))
    return None

def print_maze_path(path):
    maze_copy = copy.deepcopy(maze)
    for r, c in path:
        if maze_copy[r][c] not in ['S', 'E']:
            maze_copy[r][c] = '*'

    print("\nSolved Maze:")
    for row in maze_copy:
        print(' '.join(row))

def main():
    start = find_start()
    if not start:
        print("Start point 'S' not found in the maze.")
        return

    path = bfs(start)
    if path:
        print("Path found!")
        print_maze_path(path)
    else:
        print("No path found from 'S' to 'E'.")

if __name__ == "__main__":
    main()