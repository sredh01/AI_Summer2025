# Assignment One – Tic Tac Toe (Python + Tkinter)

**Author:** Redhouse  
**Course:** AI Summer 2025  
**Assignment:** GUI Tic Tac Toe  
**Date:** June 9, 2025

---

## Description

This project implements a simple, interactive Tic-Tac-Toe game using **Python** and the **Tkinter GUI library**, following the object-oriented programming model described in the assignment one prompt.

The program creates a 3×3 grid of clickable cells, each managed by a `Cell` class that extends `tk.Label`. Players alternate turns by clicking on empty cells, and the game displays popup messages when a player wins or the game ends in a tie.

---

## Core Features

- GUI built with **Tkinter**
- Each cell is a `Cell` object with:
  - An image (`empty.gif`, `x.gif`, or `o.gif`)
  - A `token` variable representing the state (`" "`, `"X"`, or `"O"`)
  - A click-bound `flip()` method
- Turn tracking using a global `token_variable`
- Win condition detection (rows, columns, diagonals)
- Full board (tie) detection
- Game state freezes on win or draw
- Messages displayed via `messagebox.showinfo()`

---

## Project Structure
```plaintext
AssignmentOne_Tic_Tac_Toe/
├── main.py         # Game logic and GUI implementation
└── image/          # Provided image assets
    ├── empty.gif
    ├── x.gif
    └── o.gif
```
---

## Gameplay Logic

- Each cell starts with `empty.gif` and token `" "`.
- Clicking an empty cell sets its token to `"X"` or `"O"`, updates its image, and switches turns.
- After each move, `isWon()` checks for a win and returns the winning token, if any.
- If the board is full and no one has won, `isFull()` triggers a "Game Over" message.

### Key Functions

- `Cell.flip(self, event)` – handles click logic and state/image updates.
- `isWon()` – checks all win conditions and returns the winning player.
- `isFull()` – returns `True` if the board has no empty cells left.

---

## Demo
![AssignmentOne](https://github.com/user-attachments/assets/ed2fc975-ce97-467e-a4c1-aa79fb2f38e5)
---

## Assignment Criteria Overview

| Requirement               | Status |
|---------------------------|--------|
| OOP-based solution using `Cell` class | Yes |
| GUI with Tkinter using image assets  | Yes |
| Click-to-play and turn tracking      | Yes |
| Win and full-board logic             | Yes |
| Message display using `messagebox`   | Yes |
| Code within 100 lines (functional)   | Yes |
| Header comments in source code       | Included |
| Inline comments for clarity          | Included |
| Demonstration video                  | Included |

---

## Notes

This submission was completed per assignment guidelines:
- Used the provided image assets
- Followed the suggested class design and logic structure
- Game logic completed within 100 lines (excluding comments and whitespace)
- Final result tested and verified working on macOS (M1 Pro 2021) using Python 3.12

---

## License

This repository is part of a course submission and is intended for academic use only.


