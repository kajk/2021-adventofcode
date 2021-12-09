#! /usr/bin/env python3

from colorama import Fore, Style
from typing import Iterable, Tuple


def yield_neighbours(row: int, col: int, grid) -> Iterable[Tuple[int, int, int]]:
    if row - 1 >= 0:
        yield grid[row - 1][col], row -1, col
    if row + 1 < len(grid):
        yield grid[row + 1][col], row + 1, col
    if col - 1 >= 0:
        yield grid[row][col - 1], row, col -1
    if col + 1 < len(grid[0]):
        yield grid[row][col + 1], row, col + 1


def check_neighbours(row: int, col: int, grid) -> bool:
    value = grid[row][col]
    return all(value < n for n, _, _ in yield_neighbours(row, col, grid))


class Basin:
    def __init__(self, row: int, col: int, lowest: int, grid):
        self.row = row
        self.col = col
        self.lowest = lowest
        self.coordinates = self._calculate_size(grid)
        self.size = len(self.coordinates) - 1

    def _calculate_size(self, grid) -> int:
        todo = [(self.row, self.col)]
        result = [todo]
        idx = 0
        while len(todo) != 0:
            row, col = todo.pop()
            for elm, row_idx, col_idx in yield_neighbours(row, col, grid):
                if (row_idx, col_idx) not in result and int(elm) != 9:
                    result.append((row_idx, col_idx))
                    todo.append((row_idx, col_idx))
        return result

    def print_marked_grid(self, grid):
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if (row_idx, col_idx) in self.coordinates:
                    print(Fore.CYAN + str(col) + Style.RESET_ALL, end='')
                else:
                    print(str(col), end='')
            print()

def main():
    with open('input') as fp:
        grid = [line.strip() for line in fp.readlines()]
        basins = []
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                l = check_neighbours(row_idx, col_idx, grid)
                if l:
                    basins.append(Basin(row_idx, col_idx, col, grid))
                    print(Fore.CYAN + col + Style.RESET_ALL, end='')
                else:
                    print(col, end='')
            print()
        print('----')
        for b in basins:
            b.print_marked_grid(grid)
            print(f'----- {b.size}')
        result = 1
        for idx, b in enumerate(sorted(basins, key=lambda e: e.size, reverse=True)):
            if idx > 2:
                break
            print(b.size)
            result *= b.size
        print(f'Result: {result}')


def main_part1():
    with open('input') as fp:
        lines = [line.strip() for line in fp.readlines()]
        lowest = []
        for row_idx, row in enumerate(lines):
            for col_idx, col in enumerate(row):
                l = check_neighbours(row_idx, col_idx, lines)
                if l:
                    lowest.append(int(col))
                    print(Fore.CYAN + col + Style.RESET_ALL, end='')
                else:
                    print(col, end='')
            print()
        print(lowest)
        result = sum(i + 1 for i in lowest)
        print(f'Result: {result}')


if __name__ == '__main__':
    main()
