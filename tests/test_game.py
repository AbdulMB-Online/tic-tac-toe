from game import Game


def test_game_initialization():
    game = Game()

    assert game.current_player == "X"
    assert game.winner is None
    assert game.game_over == False
    assert game.is_draw == False


def test_turn_switching():
    game = Game()

    game.make_move(0, 0)
    assert game.current_player == "O"

    game.make_move(0, 1)
    assert game.current_player == "X"


def test_invalid_move():
    game = Game()

    game.make_move(0, 0)
    assert game.make_move(0, 0) == False

    assert game.current_player == "O"
    assert game.board.cell(0, 0) == "X"


def test_out_of_bounds_move():
    game = Game()

    assert game.make_move(3, 3) == False
    assert game.make_move(-1, 0) == False
    assert game.current_player == "X"


def test_player_wins():
    game = Game()

    game.make_move(0, 0)
    game.make_move(1, 0)
    game.make_move(0, 1)
    game.make_move(1, 1)
    game.make_move(0, 2)

    assert game.winner == "X"
    assert game.game_over == True
    assert game.is_draw == False


def test_draw():
    game = Game()

    moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2)
    ]

    for row, col in moves:
        game.make_move(row, col)

    assert game.is_draw == True
    assert game.game_over == True
    assert game.winner is None


def test_move_after_game_over():
    game = Game()

    game.make_move(0, 0)
    game.make_move(1, 0)
    game.make_move(0, 1)
    game.make_move(1, 1)
    game.make_move(0, 2)

    assert game.make_move(2, 2) == False
    assert game.board.cell(2, 2) == " "