import main


def test_player_x_wins(monkeypatch, capsys):
    inputs = iter(["1", "1 1", "2 1", "1 2", "2 2", "1 3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.main()

    output = capsys.readouterr().out
    assert "Player X wins!" in output


def test_invalid_menu(monkeypatch, capsys):
    inputs = iter(["3", "1", "1 1", "2 1", "1 2", "2 2", "1 3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.main()

    output = capsys.readouterr().out
    assert "Invalid choice" in output


def test_invalid_move(monkeypatch, capsys):
    inputs = iter(["1", "1 1", "1 1", "2 1", "1 2", "2 2", "1 3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.main()

    output = capsys.readouterr().out
    assert "Invalid move" in output
    assert "Player X wins!" in output


def test_invalid_input(monkeypatch, capsys):
    inputs = iter(["1", "abc", "1 1", "2 1", "1 2", "2 2", "1 3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.main()

    output = capsys.readouterr().out
    assert "Invalid input" in output
    assert "Player X wins!" in output


def test_draw(monkeypatch, capsys):
    inputs = iter([
        "1", "1 1", "1 2", "1 3",
        "2 2", "2 1", "2 3",
        "3 2", "3 1", "3 3"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.main()

    output = capsys.readouterr().out
    assert "It's a draw!" in output