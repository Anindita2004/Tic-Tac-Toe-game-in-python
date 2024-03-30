import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Function to handle button clicks
def on_button_click(index):
    global current_player, game_over

    if board[index] == " " and not game_over:
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            game_over = True
        elif " " not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to check for a winner
def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=("normal", 20), height=2, width=5, command=lambda i=i: on_button_click(i))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

# Start the game
window.mainloop()