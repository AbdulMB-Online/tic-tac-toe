from game import Game

def main():
    """Run a two-player Tic-Tac-Toe game."""

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print("1. Two Players")
        choice = input("Enter your choice: ")

        if choice == "1":
            break

        print("Invalid choice. Please enter 1.")

    game = Game()
    print(game.board)

    while not game.game_over:
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
        print(f"Player {game.winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()