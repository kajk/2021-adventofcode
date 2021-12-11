
from typing import Any, Iterable, Tuple


def yield_neighbours(row: int, col: int, grid: list[list[Any]]) -> Iterable[Tuple[Any, int, int]]:
    if row - 1 >= 0:
        yield grid[row - 1][col], row -1, col
    if row + 1 < len(grid):
        yield grid[row + 1][col], row + 1, col
    if col - 1 >= 0:
        yield grid[row][col - 1], row, col -1
    if col + 1 < len(grid[0]):
        yield grid[row][col + 1], row, col + 1


def yield_all_neighbours(row: int, col: int, grid: list[list[Any]]) -> Iterable[Tuple[Any, int, int]]:
    # row + 1
    if row - 1 >= 0:
        yield grid[row - 1][col], row - 1, col
        if col - 1 >= 0:
            yield grid[row - 1][col - 1], row - 1, col -1
        if col + 1 < len(grid[0]):
            yield grid[row - 1][col + 1], row - 1, col + 1
    # == row
    if col - 1 >= 0:
        yield grid[row][col - 1], row, col -1
    if col + 1 < len(grid[0]):
        yield grid[row][col + 1], row, col + 1
    # row + 1
    if row + 1 < len(grid):
        yield grid[row + 1][col], row + 1, col
        if col - 1 >= 0:
            yield grid[row + 1][col - 1], row + 1, col -1
        if col + 1 < len(grid[0]):
            yield grid[row + 1][col + 1], row + 1, col + 1


def yield_grid_elms(grid: list[list[Any]]) -> Iterable[Any]:
    return (elm for sublist in grid for elm in sublist)


def yield_grid(grid: list[list[Any]]) -> Iterable[Tuple[Any, int, int]]:
    for row_idx, row in enumerate(grid):
        for col_idx, elm in enumerate(row):
            yield row_idx, col_idx, elm

