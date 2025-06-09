import os, sys
import tkinter as tk
from tkinter import messagebox

# Main window setup
window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("Assignment One - S. Redhouse")

label = tk.Label(window, text="Tic Tac Toe")
label.pack(pady=10)

# Create a frame to center the grid
game_frame = tk.Frame(window)
game_frame.pack(expand=True)

# Load images
empty_gif = tk.PhotoImage(file="image/empty.gif")
x_gif = tk.PhotoImage(file="image/x.gif")
y_gif = tk.PhotoImage(file="image/o.gif")

token_variable = "X"
cells = []


# Restart program
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Show game over message and restart
def game_over_popup(msg):
    if messagebox.showinfo("Game Over", msg, parent=window) == "ok":
        window.destroy()
        restart_program()


# Win check
def isWon():
    global token_variable
    # Check each row
    for i in range(3):
        if cells[i][0].token == cells[i][1].token == cells[i][2].token != " ":
            token_variable = "Over"
            return cells[i][0].token
    # Check each column
    for j in range(3):
        if cells[0][j].token == cells[1][j].token == cells[2][j].token != " ":
            token_variable = "Over"
            return cells[0][j].token
    # Check backslash diagonal \
    if cells[0][0].token == cells[1][1].token == cells[2][2].token != " ":
        token_variable = "Over"
        return cells[0][0].token
    # Check forward slash diagonal /
    if cells[0][2].token == cells[1][1].token == cells[2][0].token != " ":
        token_variable = "Over"
        return cells[0][2].token
    return None


# Full board check
def isFull():
    return all(cells[i][j].token != " " for i in range(3) for j in range(3))


# Cell class
class Cell(tk.Label):
    def __init__(self, master, row, col):
        super().__init__(master, image=empty_gif, width=120, height=120, borderwidth=1, relief="solid")
        self.token = " "
        self.grid(row=row, column=col)
        self.bind("<Button-1>", self.flip)

    def flip(self, event):
        global token_variable
        if self.token == " " and token_variable != "Over":
            self.config(image=x_gif if token_variable == "X" else y_gif)
            self.token = token_variable
            token_variable = "O" if self.token == "X" else "X"
            # Update before showing message box so x appears before the winner or tie message box is shown.
            window.update_idletasks()
            winner = isWon()
            if winner:
                game_over_popup(f"{winner} wins!")
            elif isFull():
                token_variable = "Over"
                game_over_popup("It's a tie!")


# Build the board
for i in range(3):
    row = []
    for j in range(3):
        row.append(Cell(game_frame, i, j))
    cells.append(row)

window.mainloop()
