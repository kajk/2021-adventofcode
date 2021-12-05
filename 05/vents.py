#! /usr/bin/env python3
import re
from typing import Iterable, Tuple


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


def parse_line(line: str) -> Tuple[int, int, int, int]:
    first, second = line.split(' -> ')
    first_split = first.split(',')
    second_split = second.split(',')
    return int(first_split[0]), int(first_split[1]), int(second_split[0]), int(second_split[1])


class Field:
    def __init__(self):
        self.visited_count = 0

    def increment(self):
        self.visited_count += 1

    def __str__(self):
        if self.visited_count == 0:
            return '.'
        else:
            return str(self.visited_count)


class Grid:
    def __init__(self):
        self.grid: dict[int, dict[int, Field]] = {}
        self.height = 0
        self.width = 0

    def _increment_coordinate(self, col_idx: int, row_idx: int):
        try:
            outer = self.grid[row_idx]
        except KeyError:
            outer = {}
            self.grid[row_idx] = outer
            if row_idx > self.height:
                self.height = row_idx
        try:
            inner = outer[col_idx]
        except KeyError:
            inner = Field()
            outer[col_idx] = inner
            if col_idx > self.width:
                self.width = col_idx
        inner.increment()

    def consume_vent(self, col1: int, row1: int, col2: int, row2: int):
        if col1 == col2:
            print(f'Horizontal line {col1},{row1} -> {col2},{row2}')
            for idx in range(abs(row1 - row2) + 1):
                self._increment_coordinate(col1, min(row1, row2) + idx)
        elif row1 == row2:
            print(f'Vertical line {col1},{row1} -> {col2},{row2}')
            for idx in range(abs(col1 - col2) + 1):
                self._increment_coordinate(min(col1, col2) + idx, row1)
        else:
            print(f'Skipping line {col1},{row1} -> {col2},{row2}')

    def print_grid(self):
        default_field = Field()
        for row_idx in range(self.height + 1):
            row = self.grid.get(row_idx, {})
            for col_idx in range(self.width + 1):
                field = row.get(col_idx, default_field)
                print(str(field), end='')
            print()

    def count_double_visited(self):
        result = 0
        for row in self.grid.values():
            for col in row.values():
                if col.visited_count >= 2:
                    result += 1
        return result


def main():
    grid = Grid()
    for line in yield_file('input'):
        col1, row1, col2, row2 = parse_line(line)
        grid.consume_vent(col1, row1, col2, row2)
    grid.print_grid()
    print(f'Dangerous Areas: {grid.count_double_visited()}')


if __name__ == "__main__":
    main()
