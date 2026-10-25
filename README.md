# Tic-Tac-Toe with AI Opponent

## About the Game

A Python-based Tic-Tac-Toe game that runs in the terminal. Players can choose to play against another person or against a computer opponent.

The game supports two difficulty levels:

- **Easy:** The computer selects a random available cell.
- **Hard:** The computer uses the Minimax algorithm to make optimal moves and avoid losing.

The game uses a 3×3 board, with X always playing first. It detects wins, draws, and invalid moves.

## Requirements

- Python 3.10 or later
- pytest

## Installation

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/AbdulMB-Online/tic-tac-toe.git
cd tic-tac-toe
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```



## How to Run the Game

Run the following command from the project directory:

```bash
python main.py
```

Choose a game mode:

1. Two Players
2. Play Against Computer

If playing against the computer, select Easy or Hard difficulty.

Enter moves using row and column numbers from 1 to 3, separated by a space.

Example:

```text
Player X (row col): 1 2
```

Invalid moves are rejected without losing the player's turn. The game continues until a player wins or the board is full.

## How to Run Tests

The project uses pytest for automated testing.

Run all tests from the project directory:

```bash
python -m pytest -v
```

The tests cover:

- Board initialization and valid moves
- Invalid and occupied cells
- Winning combinations and draws
- Turn switching and game state
- Easy AI random moves and seeded randomness
- Hard AI winning and blocking moves
- Hard AI never losing
- Board preservation during AI move selection



## Continuous Integration

GitHub Actions automatically runs the tests when a pull request is opened or changes are pushed to the main branch.

The workflow is located at `.github/workflows/ci.yml`.