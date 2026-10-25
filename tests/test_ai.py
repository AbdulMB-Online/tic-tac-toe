import random
import pytest
from board import Board
from ai import AIPlayer, EasyAI, HardAI


def test_abstract_ai():
    with pytest.raises(TypeError):
        AIPlayer(random.Random(42))


def test_easy_ai_valid_move():
    board = Board()
    board.place_mark(0, 0, "X")

    ai = EasyAI(random.Random(42))
    move = ai.choose_move(board, "O")

    assert move in board.empty_cells()


def test_easy_ai_seeded():
    board = Board()

    ai1 = EasyAI(random.Random(42))
    ai2 = EasyAI(random.Random(42))

    assert ai1.choose_move(board, "O") == ai2.choose_move(board, "O")


def test_easy_ai_full_board():
    board = Board()

    for row in range(3):
        for col in range(3):
            board.place_mark(row, col, "X")

    ai = EasyAI(random.Random(42))

    with pytest.raises(ValueError):
        ai.choose_move(board, "O")


def test_hard_ai_winning_move():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 0, "O")
    board.place_mark(1, 1, "O")

    ai = HardAI(random.Random(42))

    assert ai.choose_move(board, "O") == (1, 2)


def test_hard_ai_blocks_opponent():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 1, "O")

    ai = HardAI(random.Random(42))

    assert ai.choose_move(board, "O") == (0, 2)


def test_ai_does_not_modify_board():
    board = Board()
    board.place_mark(0, 0, "X")

    original = board.copy()

    for ai_class in (EasyAI, HardAI):
        ai = ai_class(random.Random(42))
        ai.choose_move(board, "O")

        for row in range(3):
            for col in range(3):
                assert board.cell(row, col) == original.cell(row, col)

def test_hard_ai_never_loses():
    ai = HardAI(random.Random(42))

    def play_game(board):
        if board.has_won("O") or board.is_full():
            return

        for row, col in board.empty_cells():
            new_board = board.copy()
            new_board.place_mark(row, col, "X")

            assert not new_board.has_won("X")

            if new_board.is_full():
                continue

            move = ai.choose_move(new_board, "O")
            assert move in new_board.empty_cells()

            new_board.place_mark(move[0], move[1], "O")

            if not new_board.has_won("O"):
                play_game(new_board)

    play_game(Board())                