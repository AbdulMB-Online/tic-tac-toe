from board import Board, EMPTY

def test_initial_board():
    board = Board()
    assert board.size == 3
    assert board.cell(0, 0) == EMPTY
    assert len(board.empty_cells()) == 9


def test_place_mark():
    board = Board()
    assert board.place_mark(0, 0, "X") == True
    assert board.cell(0, 0) == "X"
    assert board.place_mark(0, 0, "O") == False


def test_remove_mark():
    board = Board()
    board.place_mark(0, 0, "X")
    board.remove_mark(0, 0)
    assert board.cell(0, 0) == EMPTY


def test_has_won():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(0, 2, "X")
    assert board.has_won("X") == True
    assert board.has_won("O") == False

def test_empty_cells():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(0, 2, "X")
    assert len(board.empty_cells()) == 6

def test_no_winner():
    board = Board()

    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "O")
    board.place_mark(1, 1, "X")

    assert board.has_won("X") is False
    assert board.has_won("O") is False


def test_full_board():
    board = Board()

    assert board.is_full() is False

    for row in range(3):
        for col in range(3):
            board.place_mark(row, col, "X")

    assert board.is_full() is True
    assert len(board.empty_cells()) == 0


def test_draw():
    board = Board()

    moves = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]

    for row in range(3):
        for col in range(3):
            board.place_mark(row, col, moves[row][col])

    assert board.is_full() is True
    assert board.has_won("X") is False
    assert board.has_won("O") is False


def test_independent_copy():
    board = Board()
    board.place_mark(0, 0, "X")

    copied_board = board.copy()

    assert copied_board is not board
    assert copied_board.cell(0, 0) == "X"

    copied_board.place_mark(1, 1, "O")

    assert copied_board.cell(1, 1) == "O"
    assert board.cell(1, 1) == EMPTY

    board.place_mark(2, 2, "X")

    assert copied_board.cell(2, 2) == EMPTY