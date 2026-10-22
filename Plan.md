# 1. **GOAL**:
This project aims to create a terminal-based Tic-Tac-Toe game. It supports two players or one player against a computer opponent. 
There are two difficulty levels - Easy or Hard. The human player always start with 'X' and the computer plays 'O'. In Easy - the computer picks a random cell whereas, in Hard - It uses the minimax algorithm and never loses when it plays second.

# 2. **Requirements**:
| ID | Requirement | How to Verify |
|---|---|---|
| R1 | A new game starts with an empty 3x3 board. | Create a Board and verify all nine cells are empty. |
| R2 | Invalid moves are rejected without losing the player's turn. | Test occupied cells, out-of-bounds positions, and non-numeric input. |
| R3 | Player X always starts, and turns alternate between X and O. | Make several valid moves and verify the correct player takes each turn. |
| R4 | The game detects horizontal, vertical, and diagonal wins. | Test winning combinations across rows, columns, and both diagonals. |
| R5 | Easy AI randomly selects an available cell. | Use a seeded random generator and verify the AI always chooses an empty cell. |
| R6 | Hard AI uses minimax and never loses when playing second. | Test winning and blocking moves, and verify it never loses against any possible X strategy. |

# 3. **Components**:
**Board**: This is where the game board is managed. It ensures all moves are within the 3×3 grid and that cells are not already occupied. It updates and maintains the board's state as the game progresses. It also checks for winning conditions and whether the board is full.

**AI base class**: Defines a common interface for all AI opponents using the choose_move(board, mark) method. It takes the current board state and the AI player's mark ('X' or 'O') and requires each AI subclass to implement its own move-selection strategy.

**EasyAI**: It comes into the picture when the user choses to play against computer in the easy mode, it plays 'O' and choses moves at random

**HardAI**: It is triggered when the user choses to play against computer in the hard mode, it uses the minimax algorithm to play and never loses when it goes second

**Game**: The game coordinates across game modes and difficulty levels. It ensures invalid inputs don't cost turns to the player.

**main.py**: It takes the user input then converts it into valid tic-tac-toe move. it also holds the prompts and is responsible for printing the board after each and every move.



# 4. **Decision**:
**Decision 1**: Board Representation

Options considered:

A) A 2D list to represent the rows and columns.

B) A 1D list to store all nine cells.

Chosen approach: A 

Reason: The requirements mention place_mark(row, col, mark) which is better possible with a 2d list. Also for vlaidation logic for a win will be more structured and simpler with a 2D list.

**Decision 2**: Separation of Responsibilities

Options considered:

A) A single class responsible for all game functionality.

B) Multiple classes, each with a specific responsibility.

Chosen approach: B

Reason: Using multiple classes, each with a specific responsibility, is better when building a Tic Tac Toe game because it separates tasks such as managing the board, handling player moves, and checking win conditions. This makes the game easier to understand, debug, test, modify, and maintain without affecting other parts of the code.