import tkinter as tk


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

window = tk.Tk()
window.title("Sudoku Solver")

cell_size = 60
board_size = cell_size * 9

canvas = tk.Canvas(window, width=board_size, height=board_size)
canvas.pack()

def draw_board():
    canvas.delete("all")

    for row in range(9):
        for col in range(9):
            cell_value = board[row][col]
            cell_x = col * cell_size
            cell_y = row * cell_size

            canvas.create_rectangle(cell_x, cell_y, cell_x + cell_size, cell_y + cell_size, outline="black")

            if cell_value != 0:
                canvas.create_text(cell_x + cell_size // 2, cell_y + cell_size // 2, text=str(cell_value),
                                   font=("Arial", 20))

    for i in range(10):
        line_color = "black" if i % 3 == 0 else "red"

        canvas.create_line(0, i * cell_size, board_size, i * cell_size, fill=line_color)
        canvas.create_line(i * cell_size, 0, i * cell_size, board_size, fill=line_color)

def is_valid(row, col, num):
    
    for i in range(9):
        if board[row][i] == num:
            return False

 
    for i in range(9):
        if board[i][col] == num:
            return False

  
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num):
                        board[row][col] = num
                        draw_board()
                        window.update()

                        if solve_sudoku():
                            return True

                        board[row][col] = 0
                        draw_board()
                        window.update()

                return False

    return True

def solve_button_click():
    solve_sudoku()

draw_board()


solve_button = tk.Button(window, text="Solve", command=solve_button_click)
solve_button.pack()


window.mainloop()
