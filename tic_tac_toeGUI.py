import tkinter as tk
from tkinter import messagebox

 
player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]

 
window = tk.Tk()
window.title("Tic Tac Toe")

 
def handle_click(row, col):
    global player
    if board[row][col] == " ":
        board[row][col] = player
        buttons[row][col].configure(text=player)
        if has_won(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

 
def has_won(player):
     
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True

     
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

     
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

 
def is_board_full():
    return all(board[row][col] != " " for row in range(3) for col in range(3))

 
def reset_game():
    global player, board
    player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(text=" ", state="normal")

 
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=" ", width=10, height=5, command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

 
window.mainloop()
