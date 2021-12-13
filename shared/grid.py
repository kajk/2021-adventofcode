from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar('T')  # Any type.

class LazyGrid(Generic[T]):
    def __init__(self):
        self.grid = {}
        self.max_row = 0
        self.max_col = 0

    def set(self, row: int, col: int, value: T):
        self.grid[(row, col)] = value
        if row > self.max_row:
            self.max_row = row
        if col > self.max_col:
            self.max_col = col

    def get(self, row: int, col: int):
        return self.grid.get((row, col))

    @property
    def row_size(self):
        return self.max_row

    @property
    def col_size(self):
        return self.max_col

    def yield_grid(self, default: T | None = None) -> Iterable[Tuple[int, int, T | None]]:
        for row_idx in range(self.max_row + 1):
            for col_idx in range(self.max_col + 1):
                yield row_idx, col_idx, self.grid.get((row_idx, col_idx), default)
