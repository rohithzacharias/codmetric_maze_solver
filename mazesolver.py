import tkinter as tk
from tkinter import messagebox

# Maze Definition
maze = [
    ['S', ' ', '#', ' ', ' ', 'E'],
    ['#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#']
]

ROWS = len(maze)
COLS = len(maze[0])
CELL_SIZE = 50

# Find Start Position
for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == 'S':
            player_pos = [i, j]

# GUI Setup
root = tk.Tk()
root.title("Maze Game - GUI")

canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
canvas.pack()

# Draw the Maze Grid
def draw_maze():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1 = c * CELL_SIZE
            y1 = r * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if maze[r][c] == '#':
                color = "black"
            elif maze[r][c] == 'E':
                color = "green"
            elif maze[r][c] == 'S':
                color = "lightblue"
            else:
                color = "white"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    # Draw Player
    pr, pc = player_pos
    x = pc * CELL_SIZE + CELL_SIZE // 2
    y = pr * CELL_SIZE + CELL_SIZE // 2
    canvas.create_oval(x-15, y-15, x+15, y+15, fill="red")

# Move Function
def move(dr, dc):
    r, c = player_pos
    nr, nc = r + dr, c + dc

    if 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] != '#':
        player_pos[0], player_pos[1] = nr, nc
        draw_maze()

        if maze[nr][nc] == 'E':
            messagebox.showinfo("🎉 You Win!", "Congratulations! You've reached the end of the maze.")
            root.quit()

# Control Buttons with Labels
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="⬆️ Up (W)", width=12, command=lambda: move(-1, 0)).grid(row=0, column=1)
tk.Button(control_frame, text="⬅️ Left (A)", width=12, command=lambda: move(0, -1)).grid(row=1, column=0)
tk.Button(control_frame, text="➡️ Right (D)", width=12, command=lambda: move(0, 1)).grid(row=1, column=2)
tk.Button(control_frame, text="⬇️ Down (S)", width=12, command=lambda: move(1, 0)).grid(row=2, column=1)

# Initial draw
draw_maze()

root.mainloop()