import random
from game import Game
from ai import EasyAI, HardAI


def main():
    """Run a Tic-Tac-Toe game with two players or against AI."""

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print("1. Two Players")
        print("2. Play Against Computer")
        choice = input("Enter your choice: ")

        if choice in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    ai = None

    if choice == "2":
        while True:
            print("1. Easy")
            print("2. Hard")
            difficulty = input("Choose difficulty: ")

            if difficulty in ("1", "2"):
                break

            print("Invalid choice. Please enter 1 or 2.")

        rng = random.Random()

        if difficulty == "1":
            ai = EasyAI(rng)
        else:
            ai = HardAI(rng)

    game = Game(ai)
    print(game.board)

    while not game.game_over:

        if game.ai is not None and game.current_player == "O":
            game.computer_move()
            print("Computer played:")
            print(game.board)
            continue

        try:
            row, col = map(int, input(
                f"Player {game.current_player} (row col): "
            ).split())
        except ValueError:
            print("Invalid input. Enter two numbers.")
            continue

        if not game.make_move(row - 1, col - 1):
            print("Invalid move. Try again.")
            continue

        print(game.board)

    if game.winner:
        if game.ai is not None and game.winner == "O":
            print("Computer wins!")
        else:
            print(f"Player {game.winner} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()