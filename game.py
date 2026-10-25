from board import Board


class Game:
    """Manage turns, moves, and the result of a Tic-Tac-Toe game."""

    def __init__(self, ai=None):
        self.board = Board()
        self.current_player = "X"
        self.ai = ai
        self.winner = None
        self.is_draw = False
        self.game_over = False

    def make_move(self, row, col):
        """Place a mark and update the game state."""

        if self.game_over:
            return False

        if not self.board.place_mark(row, col, self.current_player):
            return False

        if self.board.has_won(self.current_player):
            self.winner = self.current_player
            self.game_over = True

        elif self.board.is_full():
            self.is_draw = True
            self.game_over = True

        else:
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

        return True

    def computer_move(self):
        """Ask the AI to choose a move and apply it."""

        if self.ai is None or self.current_player != "O" or self.game_over:
            return False

        row, col = self.ai.choose_move(self.board, "O")
        return self.make_move(row, col)