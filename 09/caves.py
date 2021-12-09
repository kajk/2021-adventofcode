#! /usr/bin/env python3

from colorama import Fore, Style
from typing import Iterable


def yield_neighbours(row: int, col: int, grid) -> Iterable[int]:
    if row - 1 >= 0:
        yield grid[row - 1][col]
    if row + 1 < len(grid):
        yield grid[row + 1][col]
    if col - 1 >= 0:
        yield grid[row][col - 1]
    if col + 1 < len(grid[0]):
        yield grid[row][col + 1]


def check_neighbours(row: int, col: int, grid) -> bool:
    value = grid[row][col]
    return all(value < n for n in yield_neighbours(row, col, grid))


def main():
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
