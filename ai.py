from abc import ABC, abstractmethod
from board import Board


class AIPlayer(ABC):
    """Abstract base class for AI players."""

    def __init__(self, rng):
        self.rng = rng

    @abstractmethod
    def choose_move(self, board, mark):
        """Return the row and column of the chosen move."""
        pass


class EasyAI(AIPlayer):
    """Choose a random empty cell."""

    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        """Return a randomly selected empty cell."""

        empty_cells = board.empty_cells()

        if not empty_cells:
            raise ValueError("No empty cells available.")

        return self.rng.choice(empty_cells)


class HardAI(AIPlayer):
    """Choose the best move using the minimax algorithm."""

    def choose_move(self, board, mark):

        empty_cells = board.empty_cells()

        if not empty_cells:
            raise ValueError("No empty cells available.")

        best_score = -2
        best_move = None
        opponent = "O" if mark == "X" else "X"
        temp_board = board.copy()

        for row, col in temp_board.empty_cells():
            temp_board.place_mark(row, col, mark)

            if temp_board.has_won(mark):
                temp_board.remove_mark(row, col)
                return (row, col)

            score = self._minimax(temp_board, opponent, mark)

            temp_board.remove_mark(row, col)

            if score > best_score:
                best_score = score
                best_move = (row, col)

        return best_move

    def _minimax(self, board, turn, ai_mark):
        opponent = "O" if ai_mark == "X" else "X"

        if board.has_won(ai_mark):
            return 1

        if board.has_won(opponent):
            return -1

        if board.is_full():
            return 0

        scores = []

        for row, col in board.empty_cells():
            board.place_mark(row, col, turn)

            next_turn = "O" if turn == "X" else "X"
            score = self._minimax(board, next_turn, ai_mark)

            board.remove_mark(row, col)
            scores.append(score)

        if turn == ai_mark:
            return max(scores)

        return min(scores)    