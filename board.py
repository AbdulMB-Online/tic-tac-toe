EMPTY = " "

class Board:
    """A square Tic-Tac-Toe board."""

    def __init__(self):
        self._size = 3
        self._grid = [[EMPTY] * 3 for _ in range(3)] 
        

    @property
    def size(self):
        return self._size

    def cell(self, row, col):
        """Return the mark at row, col (counting from 0)."""
        return self._grid[row][col]

    def _in_range(self, row, col):
        return 0 <= row < self._size and 0 <= col < self._size

    def place_mark(self, row, col, mark):
        """Place mark at row, col. Return True if placed, False if not allowed."""
        if not self._in_range(row, col):
            return False
        if self._grid[row][col] != EMPTY:
            return False
        self._grid[row][col] = mark
        return True

    def empty_cells(self):
        """Return a list of (row, col) pairs for every empty cell."""
        return [(r, c) for r in range(self._size) for c in range(self._size)
                if self._grid[r][c] == EMPTY]

    def is_full(self):
        return not self.empty_cells()

    def copy(self):
        """Return an independent copy of this board."""
        clone = Board()
        clone._grid = [row[:] for row in self._grid]
        return clone

    def __str__(self):
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)

    def remove_mark(self, row, col):
        self._grid[row][col] = EMPTY

    def has_won(self, mark):
        """Return True if the player has won, otherwise False."""

        for i in range(3):
            if (self._grid[i][0] == mark and self._grid[i][1] == mark and self._grid[i][2] == mark):
                return True

            if (self._grid[0][i] == mark and self._grid[1][i] == mark and self._grid[2][i] == mark):
                return True

        if (self._grid[0][0] == mark and self._grid[1][1] == mark and self._grid[2][2] == mark):
            return True

        if (self._grid[0][2] == mark and self._grid[1][1] == mark and self._grid[2][0] == mark):
            return True

        return False
