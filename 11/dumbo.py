#! /usr/bin/env python3.9

from typing import Iterable
from colorama import Fore, Style
from shared import all_lines, endless_ints, yield_all_neighbours, \
        color, yield_grid_elms, yield_grid


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
    for row_idx, col_idx, elm in yield_grid(lines):
        grid[row_idx][col_idx] = Octopus(row_idx, col_idx, elm)
    for o in yield_grid_elms(grid):
        o.set_grid(grid)
    return grid


def step(grid):
    for o in yield_grid_elms(grid):
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


def all_flashing(grid):
    return all(elm.flashed for elm in yield_grid_elms(grid))


def main():
    lines = all_lines('input')
    grid = build_grid(lines)
    for i in endless_ints(1):
        step(grid)
        print(f'After step {i}')
        if all_flashing(grid):
            after_step(grid)
            print(f'All Flashing! on step {i}')
            break
        after_step(grid)
        print()


def main_part1():
    lines = all_lines('input')
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
