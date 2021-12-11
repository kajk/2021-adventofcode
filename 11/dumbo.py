#! /usr/bin/env python3

from typing import Iterable
from colorama import Fore, Style

def all_lines(filename: str):
    with open(filename) as fp:
        return [line.strip() for line in fp.readlines()]


def yield_all_neighbours(row, col, grid) -> Iterable:
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


def color(value):
    return Fore.CYAN + str(value) + Style.RESET_ALL


class Octopus:
    def __init__(self, row: int, col: int, initial: int):
        self.row = row
        self.col = col
        self.flashed = False
        self.grid = []
        self.level = int(initial)

    def set_grid(self, grid):
        self.grid = grid

    def _bump_neighbours(self):
        for n,_,_ in yield_all_neighbours(self.row, self.col, self.grid):
            n.step()

    def step(self):
        if not self.flashed:
            self.level += 1
            if self.level > 9:
                self.level = 0
                self.flashed = True
                self._bump_neighbours()

    def after_step(self) -> str:
        if self.flashed:
            self.flashed = False
            return color(self.level)
        else:
            return str(self.level)


def build_grid(lines):
    grid = [list(range(len(lines))) for _ in range(len(lines[0]))]
    for row_idx, row in enumerate(lines):
        for col_idx, elm in enumerate(row):
            grid[row_idx][col_idx] = Octopus(row_idx, col_idx, elm)
    for o in [elm for sublist in grid for elm in sublist]:
        o.set_grid(grid)
    return grid


def step(grid):
    for o in [elm for sublist in grid for elm in sublist]:
        o.step()


def after_step(grid):
    flashes = 0
    for row in grid:
        for o in row:
            if o.flashed:
                flashes += 1
            print(o.after_step(), end='')
        print()
    return flashes


def main():
    lines = all_lines('test.input')
    grid = build_grid(lines)
    print('Before any steps:')
    after_step(grid)
    print()
    total_flashes = 0
    for i in range(100):
        step(grid)
        print(f'After step {i + 1}')
        total_flashes += after_step(grid)
        print(f'{total_flashes=}')
        print()


if __name__ == '__main__':
    main()
