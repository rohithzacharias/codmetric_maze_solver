import os

# Define the maze
maze = [
    ['S', ' ', '#', ' ', ' ', 'E'],
    ['#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#']
]

# Find the start position
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            player_pos = [i, j]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_maze():
    clear_screen()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if [i, j] == player_pos:
                print('P', end=' ')
            else:
                print(maze[i][j], end=' ')
        print()

def move_player(direction):
    dr, dc = 0, 0
    if direction == 'w':
        dr = -1
    elif direction == 's':
        dr = 1
    elif direction == 'a':
        dc = -1
    elif direction == 'd':
        dc = 1
    else:
        return  # Invalid key

    new_r = player_pos[0] + dr
    new_c = player_pos[1] + dc

    if 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]):
        if maze[new_r][new_c] != '#':
            player_pos[0] = new_r
            player_pos[1] = new_c

def main():
    while True:
        display_maze()

        if maze[player_pos[0]][player_pos[1]] == 'E':
            print("\n🎉 Congratulations! You've reached the exit.")
            break

        move = input("Move (W/A/S/D): ").lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Invalid move. Use W (up), A (left), S (down), D (right).")
        else:
            move_player(move)

if __name__ == "__main__":
    main()