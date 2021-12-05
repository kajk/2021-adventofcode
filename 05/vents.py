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
            row = self.grid[row_idx]
        except KeyError:
            row = {}
            self.grid[row_idx] = row
            if row_idx > self.height:
                self.height = row_idx
        try:
            field = row[col_idx]
        except KeyError:
            field = Field()
            row[col_idx] = field
            if col_idx > self.width:
                self.width = col_idx
        field.increment()

    def consume_vent(self, col1: int, row1: int, col2: int, row2: int):
        for col, row in self._yield_coordinates(col1, row1, col2, row2):
            self._increment_coordinate(col, row)

    def _yield_coordinates(self, col1: int, row1: int, col2: int, row2: int) -> Tuple[int, int]:
        row_step = self._determine_step(row1, row2)
        col_step = self._determine_step(col1, col2)
        row_idx = row1
        col_idx = col1
        while row_idx != row2 + row_step or col_idx != col2 + col_step:
            yield col_idx, row_idx
            col_idx += col_step
            row_idx += row_step

    @staticmethod
    def _determine_step(one, two):
        if one < two:
            return 1
        elif one > two:
            return -1
        else:
            return 0

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
